import json

from django.utils.text import slugify
from rest_framework import pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from api.serializers.commerce import ProductSerializer
from api.serializers.store import ShopSerializer
from findit.models import Products
from shop.models import Shop


@api_view(['POST'])
def create_shop(request):
    '''
    Creates a shop for the user

    Arguments:,
        request {[request object]} -- [the neccessary data needed to create a shop]

    Returns:
        [JSON] -- [returns json if its is successful or not]
    '''

    shop = Shop.objects.filter(
        title=request.data['shopName'].lower())
    if shop.exists():
        return Response({
            'is_exist': True,
            'msg': 'This shop already exist'
        })
    shop = Shop.objects.create(
        title=request.data['shopName'].lower(),
        category=request.data['shopCategory'],
        user=request.user)
    shop.save()
    return Response({
        'is_exist': False,
        'msg': 'Success.',
        'slug': shop.slug
    })


@api_view(['GET'])
def shop_products(request):
    '''Get the products assiociated with this user shop.

    Arguments:
        request {[request object]} -- [Used as a form of verification of a user authencity]
    '''

    shop = Shop.objects.get(user=request.user)
    products = Products.objects.filter(shop_rel=shop)
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(products, request=request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def create_product(request):
    shop_obj = Shop.objects.get(user=request.user)
    data_payload = {
        'name': request.data['productName'],
        'price': request.data['productPrice'],
        'description': request.data['description'],
        'genre': json.loads(request.data['tags']),
        'image': request.data['file'],
        'shop_slug': shop_obj.slug,
        'shop_rel': shop_obj
    }
    products = Products.objects.create(**data_payload)
    products.save()
    products_serailzer = ProductSerializer(products)
    return Response(data={'product': products_serailzer.data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_tags(request):
    try:
        shop = Shop.objects.get(user=request.user)
        cat_name = request.data['categoryName'].lower()
        matches = [x for x in shop.categories if x['slug'] is cat_name]
        data_payload = {
            'name': cat_name,
            'slug': slugify(cat_name+'-'+get_random_string(length=4)) if len(matches) > 0 else slugify(cat_name)
        }
        shop.categories = [*shop.categories, data_payload]
        shop.save()
        return Response(data=data_payload, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_catergories(request):
    choosen_catergory = Shop.objects.get(user=request.user)
    shop_categories = choosen_catergory.categories
    resp_payload = {'shop_categories': shop_categories}
    return Response(data=resp_payload, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_info(request):
    user_info = Shop.objects.get(user=request.user)
    serializer = ShopSerializer(user_info)
    return Response(serializer.data)


@api_view(['POST'])
def save_info(request):
    user_info_obj = Shop.objects.get(user=request.user)
    user_info_obj.address = request.data['address']
    user_info_obj.description = request.data['description']
    if request.data['logo']:
        user_info_obj.logo = request.data['logo']
    user_info_obj.save()
    data_payload = {
        'img': user_info_obj.logo.url if user_info_obj.logo else ''
    }
    return Response(status=status.HTTP_200_OK, data=data_payload)


@api_view(['POST'])
def edit_products(request):
    try:
        products = Products.objects.get(id=request.data['id'])
        products.name = request.data['productName']
        products.price = request.data['productPrice']
        products.description = request.data['description']
        products.genre = json.loads(request.data['tags'])
        if request.data['file']:
            products.image = request.data['file']
        products.save()
        products_serailzer = ProductSerializer(products)
        return Response(status=status.HTTP_201_CREATED, data={'product': products_serailzer.data})
    except products.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_products(request):
    product_obj = Products.objects.get(id=request.data['id'])
    if request.user == product_obj.shop_rel.user:
        product_obj.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_401_UNAUTHORIZED)
