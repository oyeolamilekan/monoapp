from algoliasearch_django import raw_search
from django.core import serializers
from rest_framework import pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.commerce import ProductSerializer
from findit.models import Products
from shop.models import Shop


@api_view(['GET'])
def get_shop_info(request, slug):
    '''
        Gets the necessary info needed to show the user.

    Arguments:
        request {[request object]} -- [just for request]
        slug {[ string ]} -- [to get the needed information about the shop]

    Returns:
        [JSON] -- [Gives the user back a json response of the shop info needed]
    '''
    try:
        shop_info = Shop.objects.get(slug=slug)
        data_obj = {
            'shop_name': shop_info.title,
            'logo': shop_info.logo.url if shop_info.logo else '',
            'tags': shop_info.categories if shop_info.categories else [],
            'slug': shop_info.slug
        }
        return Response(data={'shop_info': data_obj}, status=status.HTTP_200_OK)

    except shop_info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_shop_products(request, slug, cat):
    '''
        Gets the necessary products needed to show the customer for the shop.

    Arguments:
        request {[request object]} -- [just for request]
        slug {[ string ]} -- [to get the needed information about the shop]
        cat {[ string ]} -- [to get the category for the shop]

    Returns:
        [JSON] -- [Gives the user back a json response of the shop products needed]
    '''
    shop = Shop.objects.get(slug=slug)
    products = Products.objects.filter(shop_rel=shop)
    shop_slugs = list(map(lambda x: x['slug'], shop.categories))
    if not shop.categories:
        products = []
    elif cat in shop_slugs:
        products = products.filter(genre__slug=cat)
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 6
    result_page = paginator.paginate_queryset(products, request=request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def search_query(request, slug):
    try:
        queryset = Products.objects.filter(shop_rel__slug=slug)
        query = request.GET.get('q')
        if query:
            params = {"hitsPerPage": 15}
            queryset = raw_search(Products, query, params)
            queryset = [x for x in queryset['hits'] if x['shop_slug'] == slug]
        return Response(data={'results': queryset})
    except queryset.DoesNotExist:
        return Response(data={'nothing': 'nothing'})
