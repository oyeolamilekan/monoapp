import datetime
import json

from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from analytics.models import Analytics
from findit.models import Products
from shop.models import Shop

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
    anayltics_qs = Analytics.objects.filter(
        content_type=ContentType.objects.get_for_model(product),
        object_id=product.id,
        created__gt=datetime.date.today(),
    )
    if anayltics_qs.exists():
        anayltics_obj = Analytics.objects.get(
            content_type=ContentType.objects.get_for_model(product),
            object_id=product.id,
            created__gt=datetime.date.today(),
        )
        anayltics_obj.click_count += 1
        anayltics_obj.save()
    else:
        anayltics_obj = Analytics.objects.create(content_object=product)
        anayltics_obj.save()
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product_clicks(request, pk):
    product = Products.objects.get(id=pk)
    analytics_obj = product.analytics.filter(
        created__lte=datetime.datetime.today(),
        created__gt=datetime.datetime.today() - datetime.timedelta(days=30),
    ).extra({"created": "date(created)"})
    data_set = [obj_.click_count for obj_ in analytics_obj]
    day_set = [
        datetime.datetime.strptime(str(obj_.created), "%Y-%m-%d").strftime("%a")
        for obj_ in analytics_obj
    ]
    day_set = json.dumps({"data": day_set})
    data_set = json.dumps({"data": data_set})
    return Response(
        status=status.HTTP_200_OK, data={"data_set": data_set, "day_set": day_set}
    )

@api_view(["GET"])
def get_shop_views(request, pk):
    print(pk)
    shop = Shop.objects.get(slug=pk)
    analytics_obj = shop.analytics.filter(
        created__lte=datetime.datetime.today(),
        created__gt=datetime.datetime.today() - datetime.timedelta(days=30),
    ).extra({"created": "date(created)"})
    data_set = [obj_.view_count for obj_ in analytics_obj]
    day_set = [
        datetime.datetime.strptime(str(obj_.created), "%Y-%m-%d").strftime("%a")
        for obj_ in analytics_obj
    ]
    day_set = json.dumps({"data": day_set})
    data_set = json.dumps({"data": data_set})
    return Response(
        status=status.HTTP_200_OK, data={"data_set": data_set, "day_set": day_set}
    )

@api_view(["GET"])
def create_shop_analytics(request, pk):
    shop = Shop.objects.get(pk=pk)
    anayltics_qs = Analytics.objects.filter(
        content_type=ContentType.objects.get_for_model(shop),
        object_id=shop.id,
        created__gt=datetime.date.today(),
    )
    if anayltics_qs.exists():
        anayltics_obj = Analytics.objects.get(
            content_type=ContentType.objects.get_for_model(shop),
            object_id=shop.id,
            created__gt=datetime.date.today(),
        )
        anayltics_obj.view_count += 1
        anayltics_obj.save()
    else:
        anayltics_obj = Analytics.objects.create(content_object=shop)
        anayltics_obj.save()
    return Response(status=status.HTTP_200_OK)
