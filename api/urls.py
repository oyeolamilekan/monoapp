'''
    Handles the url path for the entire app.
'''


from django.urls import path
from .views import auth_view, shop_view, user_views, store_view

app_name = 'api'

urlpatterns = [
    path('products/',
         user_views.ProductView.as_view({'get': 'list'}), name='products'),
    path(
        'phone/', user_views.ProductViewPhone.as_view({'get': 'list'}), name='phone'),
    path(
        'gaming/', user_views.GameProductView.as_view({'get': 'list'}), name='gaming'),
    path('laptops/',
         user_views.ProductViewLaptop.as_view({'get': 'list'}), name='laptops'),
    path('phone_t/',
         user_views.ProductViewPhones.as_view({'get': 'list'}), name='phone_t'),
    path('laptops_t/',
         user_views.ProductViewLaptops.as_view({'get': 'list'}), name='laptops_t'),
    path('gaming_t/',
         user_views.ProductViewGaming.as_view({'get': 'list'}), name='gaming_t'),
    path('r_search/', user_views.search_query, name='r_search'),
    path('r_redirect/<slug:id>/', user_views.number_of_clicks, name='r_redirect'),
    path('q_shop/<slug:slug>/<slug:cat>/',
         user_views.ShopProduct, name="q_shop"),
    path('create/', user_views.feedback, name='feedback'),
    path('create_o/', user_views.create_genre, name='catergory'),
    path('list/', user_views.get_user_choice, name='list'),
    path('user_products/', user_views.get_user_products, name="product_list"),
    path('register/', auth_view.RegisterAPI.as_view()),
    path('login/', auth_view.LoginAPI.as_view()),

    # Admin routes for the seller.
    path('create_shop/', shop_view.create_shop, name='create_shop'),
    path('create_tags/', shop_view.create_tags, name='create_tags'),
    path('create_product/', shop_view.create_product, name='create_product'),
    path('delete_products/', shop_view.delete_products, name='delete_products'),
    path('shop_products/', shop_view.shop_products, name='shop_products'),
    path('catergory_list/', shop_view.get_catergories, name='catergory_list'),
    path('get_info/', shop_view.get_info, name='get_info'),
    path('save_info/', shop_view.save_info, name='save_info'),
    
    # Shop routes for the customers of the sellers.
    path('shop_info/<slug:slug>/', store_view.get_shop_info, name='shop_infor'),
    path('shop_product/<slug:slug>/<slug:cat>/', store_view.get_shop_products, name='shop_products'),
    path('edit_products/', shop_view.edit_products, name='edit_produts')
]
