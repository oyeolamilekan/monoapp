import datetime
import json

from django.db.models.aggregates import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from analytics.models import Analytics
from findit.models import Products
from shop.models import Shop
from utilcode.msg.get_user_info import get_location
from utilcode.msg.ip_adress import get_client_ip

# from shop.models import Shop


@api_view(["GET"])
def create_product_analytics(request, pk):
    """[This is app will able to create counter for the product model]
    Arguments:
        request {[type]} -- [description]
        pk {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    product = Products.objects.get(id=pk)
    user_info = {
        "user_ip": request.META.get("REMOTE_ADDR", None),
        "user_phone": request.META.get("HTTP_USER_AGENT", None),
        "user_path": request.META.get("PATH_INFO", None),
        "request_method": request.META.get("REQUEST_METHOD", None),
        "request_origin": request.META.get("HTTP_ORIGIN", None),
        "user_info": get_location(get_client_ip(request)),
    }
    anayltics_obj = Analytics.objects.create(
        content_object=product, info=user_info, user=product.shop_rel.user
    )
    anayltics_obj.save()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def create_shop_analytics(request, pk):
    """[summary]
    
    Arguments:
        request {[type]} -- [description]
        pk {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    shop = Shop.objects.get(pk=pk)
    user_info = {
        "user_ip": request.META.get("REMOTE_ADDR", None),
        "user_phone": request.META.get("HTTP_USER_AGENT", None),
        "user_path": request.META.get("PATH_INFO", None),
        "request_method": request.META.get("REQUEST_METHOD", None),
        "request_origin": request.META.get("HTTP_ORIGIN", None),
        "user_info": get_location(get_client_ip(request)),
    }
    anayltics_obj = Analytics.objects.create(
        content_object=shop, info=user_info, user=shop.user
    )
    anayltics_obj.save()
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def create_tags_analytics(request):
    user_info = {
        "user_ip": request.META.get("REMOTE_ADDR", None),
        "user_phone": request.META.get("HTTP_USER_AGENT", None),
        "request_method": request.META.get("REQUEST_METHOD", None),
        "request_origin": request.META.get("HTTP_ORIGIN", None),
        "user_url": request.data["url"],
        "user_info": get_location(get_client_ip(request)),
    }
    analytics_obj = Analytics.objects.create(
        url=request.data["url"], info=user_info
    )
    analytics_obj.save()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product_clicks(request, pk):
    product = Products.objects.get(id=pk)
    analytics_obj = (
        product.analytics.extra({"created": "date(created)"})
        .values("created")
        .annotate(date_added_count=Count("id"))
        .order_by("created")
    )
    data_set = [obj_["date_added_count"] for obj_ in analytics_obj]
    day_set = [
        datetime.datetime.strptime(str(obj_["created"]), "%Y-%m-%d").strftime("%a")
        for obj_ in analytics_obj
    ]
    day_set = json.dumps({"data": day_set})
    data_set = json.dumps({"data": data_set})
    return Response(
        status=status.HTTP_200_OK, data={"data_set": data_set, "day_set": day_set}
    )


@api_view(["GET"])
def get_shop_views(request, pk):
    shop = Shop.objects.get(slug=pk)
    analytics_obj = (
        shop.analytics.extra({"created": "date(created)"})
        .values("created")
        .annotate(date_added_count=Count("id"))
        .order_by("created")
    )
    data_set = [obj_["date_added_count"] for obj_ in analytics_obj]
    day_set = [
        datetime.datetime.strptime(str(obj_["created"]), "%Y-%m-%d").strftime("%a")
        for obj_ in analytics_obj
    ]
    day_set = json.dumps({"data": day_set})
    data_set = json.dumps({"data": data_set})
    return Response(
        status=status.HTTP_200_OK, data={"data_set": data_set, "day_set": day_set}
    )


@api_view(["GET"])
def get_product_clicked(request):
    analytics = Analytics.objects.filter(
        content_type__model="products", user=request.user
    )
    products_list = [
        {"name": analytic.content_object.name, "id": str(analytic.content_object.id)}
        for analytic in analytics
    ]
    data = json.dumps(products_list)
    return Response(status=status.HTTP_200_OK, data=data)
