from django.urls import path

from ..views import analytics

ANALYTICS_URL = [
    path(
        "create_analytics_product/<slug:pk>/",
        analytics.create_product_analytics,
        name="create_analytics",
    ),
    path("get_data/<slug:pk>/", analytics.get_product_clicks, name="get_data"),
]
