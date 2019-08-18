"""
This url link is used in routing referral view page
"""

from django.urls import path

from ..views import allies

ALLIES_URL = [
    # Shop routes for the customers of the sellers.
    path("create_ally/", allies.create_ally_obj, name="create_ally_obj"),
    path("get_allies_obj/", allies.get_allies_obj, name="get_allies_obj")
]
