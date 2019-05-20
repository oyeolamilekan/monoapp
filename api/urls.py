'''
    Handles the url path for the entire app.
'''


from django.urls import path
from .views import shop_view, user_views, store_view
from .urls_route.auth import AUTH_URL
from .urls_route.commerce import COMMERCE_URL
from .urls_route.store import STORE_URL
app_name = 'api'

urlpatterns = [
    *AUTH_URL,
    *COMMERCE_URL,
    *STORE_URL
]
