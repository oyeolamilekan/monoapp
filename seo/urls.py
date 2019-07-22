from django.urls import path
from .views import get_shop_view
urlpatterns = [
    path("r/<slug:slug>/", get_shop_view, )
]

