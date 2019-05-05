from django.core import serializers
from rest_framework import pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProductSerializer
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
    shop_info = Shop.objects.get(title=slug)
    data_obj = {
        'shop_name': shop_info.title,
        'logo': shop_info.logo.url if shop_info.logo else '',
        'tags': shop_info.categories if shop_info.categories else ''
    }
    return Response(data={'shop_info': data_obj}, status=status.HTTP_200_OK)


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
    shop = Shop.objects.get(title=slug)
    products = Products.objects.filter(shop_rel=shop)
    if not shop.categories:
        products = []
    elif cat in shop.categories:
        products = products.filter(genre=cat)
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(products, request=request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
