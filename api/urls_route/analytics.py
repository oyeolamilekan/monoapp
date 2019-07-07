from django.urls import path

from ..views import analytics

ANALYTICS_URL = [
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
    )
]
