"""
    This is view is meant to handle of the user shop.
"""

import json

from django.utils.crypto import get_random_string
from django.utils.text import slugify
from rest_framework import pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

from api.serializers.commerce import ProductSerializer
from api.serializers.store import ShopSerializer
from findit.models import Products
from shop.models import Shop


@api_view(["POST"])
def create_shop(request):
    """
    Creates a shop for the user

    Arguments:,
        request {[request object]} -- [the neccessary data needed to create a shop]

    Returns:
        [JSON] -- [returns json if its is successful or not]
    """

    shop = Shop.objects.filter(title=request.data["shopName"].lower())
    if shop.exists():
        return Response({"is_exist": True, "msg": "This shop already exist"})
    shop = Shop.objects.create(
        title=request.data["shopName"].lower(),
        category=request.data["shopCategory"],
        phone_number=request.data["phoneNumber"],
        user=request.user,
    )
    shop.save()
    return Response({"is_exist": False, "msg": "Success.", "slug": shop.slug})


@api_view(["GET"])
def shop_products(request):
    """Get the products assiociated with this user shop.

    Arguments:
        request {[request object]} -- [Used as a form of verification of a user authencity]
    """

    shop = Shop.objects.get(user=request.user)
    products = Products.objects.filter(shop_rel=shop)
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 7
    result_page = paginator.paginate_queryset(products, request=request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
def create_product(request):
    """
    The create product for the shop instance
    Arguments:
        request {[ request object ]} -- this is a standard request object from django
    Returns:
        JSON -- returns a json response and info
    """
    shop_obj = Shop.objects.get(user=request.user)
    tags = json.loads(request.data["tags"])
    del tags["product_count"]
    data_payload = {
        "name": request.data["productName"],
        "price": request.data["productPrice"],
        "description": request.data["description"],
        "genre": tags,
        "image": request.data["file"],
        "shop_slug": shop_obj.slug,
        "shop_rel": shop_obj,
    }
    # Create an instance of the product
    products = Products.objects.create(**data_payload)
    # Save the product into the database
    products.save()
    products_serailzer = ProductSerializer(products)
    return Response(
        data={"product": products_serailzer.data}, status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
def create_tags(request):
    """
    Creates tags to be track products created
    Arguments:
        request { request object } -- Django request objects
    Returns:
        JSON -- returns a json response and info
    """
    try:
        shop = Shop.objects.get(user=request.user)
        cat_name = request.data["categoryName"].lower()
        matches = [x for x in shop.categories if x["slug"] == slugify(cat_name)]
        if matches:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        data_payload = {
            "name": cat_name,
            "slug": slugify(cat_name),
            "public_slug": slugify(cat_name),
        }
        shop.categories = [*shop.categories, data_payload]
        shop.save()
        return Response(data=data_payload, status=status.HTTP_201_CREATED)
    except Exception as e:
        import traceback

        traceback.print_exc()
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_catergories(request):
    """
    Calculates the number of products left in each category
    Arguments:
        request {[type]} -- [description]
    Returns:
        [Json] -- [returns a json type response]
    """
    shop_obj = Shop.objects.get(user=request.user)
    shop_categories = shop_obj.categories
    value_added = list(
        map(
            lambda x: {
                "name": x["name"],
                "slug": x["slug"],
                "public_slug": x["public_slug"],
                "product_count": Products.objects.filter(
                    shop_rel=shop_obj, genre__slug=x["slug"]
                ).count(),
            },
            shop_categories,
        )
    )
    resp_payload = {"shop_categories": value_added}
    return Response(data=resp_payload, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_info(request):
    """
    [summary]
    Arguments:
        request {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    user_info = Shop.objects.get(user=request.user)
    serializer = ShopSerializer(user_info)
    return Response(serializer.data)


@api_view(["PUT"])
def save_info(request):
    """
    This method saves the user info from the edit profile
    component
    Arguments:
        request {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    user_info_obj = Shop.objects.get(user=request.user)
    user_info_obj.address = request.data["address"]
    user_info_obj.description = request.data["description"]
    user_info_obj.phone_number = request.data["phoneNumber"]
    if request.data["logo"]:
        user_info_obj.logo = request.data["logo"]
    user_info_obj.save()
    data_payload = {"img": user_info_obj.logo.url if user_info_obj.logo else ""}
    return Response(status=status.HTTP_200_OK, data=data_payload)


@api_view(["PUT"])
def edit_products(request):
    """
    [summary]
    Arguments:
        request {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    try:
        products = Products.objects.get(id=request.data["id"])
        products.name = request.data["productName"]
        products.price = request.data["productPrice"]
        products.description = request.data["description"]
        products.genre = json.loads(request.data["tags"])
        if request.data["file"]:
            products.image = request.data["file"]
        products.save()
        products_serailzer = ProductSerializer(products)
        return Response(
            status=status.HTTP_201_CREATED, data={"product": products_serailzer.data}
        )
    except products.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_products(request):
    """
    This view deletes the product from the database.

    Arguments:
        request { Django request object } -- this is the default request object.
    Returns:
        status -- It returns a status of success, if the user is authorized
        or faliure if they aren't authorized
    """
    product_obj = Products.objects.get(id=request.data["id"])
    if request.user == product_obj.shop_rel.user:
        product_obj.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["DELETE"])
def delete_products_mobile(request, p_k):
    """
    This view deletes the product from the database. `Used only by the mobile app`

    Arguments:
        request { Django request object } -- this is the default request object.
    Returns:
        status -- It returns a status of success, if the user is authorized
        or faliure if they aren't authorized
    """
    product_obj = Products.objects.get(id=p_k)
    if request.user == product_obj.shop_rel.user:
        product_obj.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["DELETE"])
def delete_tags(request):
    """
    [summary]
    Arguments:
        request {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    shop_obj = Shop.objects.get(user=request.user)
    tags = request.data
    del tags["product_count"]
    tag_index = shop_obj.categories.index(request.data)
    del shop_obj.categories[tag_index]
    shop_obj.save()
    product_obj = Products.objects.filter(shop_rel=shop_obj, genre__slug=tags["slug"])
    product_obj.delete()
    return Response(status=status.HTTP_200_OK)
