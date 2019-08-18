"""
[This view handles all the action need for the referral app]
"""
from rest_framework import pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response

from allies.models import Allies
from api.serializers.allies import AlliesSerializer


@api_view(["POST"])
def create_ally_obj(request):
    """
    Create a referral object
    Arguments:
        request {[type]} -- [description]
    """
    data = {
        "user": request.user,
        "user_name": request.data["user_name"],
        "day_expiry": request.data["day_expiry"],
    }
    ally_obj = Allies.objects.create(**data)
    ally_obj.save()
    ally_obj_serialized = AlliesSerializer(ally_obj)
    return Response(data=ally_obj_serialized.data)


@api_view(["GET"])
def get_allies_obj(request):
    """
    This function get all allies objects.
    Arguments:
        request { request object } -- this is django request object
    Returns:
        JSON -- returns json reponse with the needed crendentials
    """
    allies = Allies.objects.filter(user=request.user).order_by("-created")
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 8
    result_page = paginator.paginate_queryset(allies, request=request)
    allies_obj = AlliesSerializer(result_page, many=True)
    return paginator.get_paginated_response(allies_obj.data)


def delete_referral_obj(request):
    pass


def edit_referral_obj(request):
    pass
