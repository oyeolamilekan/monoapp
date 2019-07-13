'''
    Handles the url path for the entire app.
'''

from .urls_route.auth import AUTH_URL
from .urls_route.commerce import COMMERCE_URL
from .urls_route.store import STORE_URL
from .urls_route.feedback import CREATE_FEEDBACK
from .urls_route.lesson import LESSON_URL
from .urls_route.comments import COMMENT_URL
from .urls_route.analytics import ANALYTICS
from .views import analytics
from django.urls import path


app_name = 'api'

urlpatterns = [
    path(
        "create_analytics_product/<slug:pk>/",
        analytics.create_product_analytics,
        name="create_product_analytics",
    ),
    path(
        "create_shop_analytics/<slug:pk>/",
        analytics.create_shop_analytics,
        name="create_shop_analytics",
    ),
    path(
        "create_tags_analytics/",
        analytics.create_tags_analytics,
        name='create_tags_analytics'
    ),
    path(
        "get_data/<slug:pk>/",
        analytics.get_product_clicks, 
        name="get_data"
    ),
    path(
        "get_shop_view/<slug:pk>/", 
        analytics.get_shop_views, 
        name="get_shop_view"
    ),
    path(
        "get_products_clicked/",
        analytics.get_product_clicked,
        name='get_products'
    ),
    *AUTH_URL,
    *COMMERCE_URL,
    *CREATE_FEEDBACK,
    *COMMENT_URL,
    *ANALYTICS,
    *LESSON_URL,
    *STORE_URL,
]
