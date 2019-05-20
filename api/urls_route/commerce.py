from django.urls import path

from ..views import shop_view

COMMERCE_URL = [
    # Admin routes for the seller.
    path('create_shop/', shop_view.create_shop, name='create_shop'),
    path('create_tags/', shop_view.create_tags, name='create_tags'),
    path('create_product/', shop_view.create_product, name='create_product'),
    path('delete_products/', shop_view.delete_products, name='delete_products'),
    path('shop_products/', shop_view.shop_products, name='shop_products'),
    path('catergory_list/', shop_view.get_catergories, name='catergory_list'),
    path('get_info/', shop_view.get_info, name='get_info'),
    path('save_info/', shop_view.save_info, name='save_info'),
    path('edit_products/', shop_view.edit_products, name='edit_produts'),
]