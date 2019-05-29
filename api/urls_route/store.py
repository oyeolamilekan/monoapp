from django.urls import path

from ..views import store_view

STORE_URL = [
    # Shop routes for the customers of the sellers.
    path('shop_info/<slug:slug>/', store_view.get_shop_info, name='shop_infor'),
    path('shop_product/<slug:slug>/<slug:cat>/',
         store_view.get_shop_products, name='shop_products'),
    path('shop_trending_products/<slug:slug>/<slug:cat>/',
         store_view.get_shop_trending_products, name="shop_trending_products"),
    path('r_search/<slug:slug>/', store_view.search_query, name="r_search")
]
