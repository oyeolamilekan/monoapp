from django.urls import path

from ..views import comments

COMMENT_URL = [
    # Tutorial routes for the merchants.
    path(
        "create_comments/<slug:slug>/<slug:content_type>/",
        comments.create_comment,
        name="create_comments",
    ),
    path(
        "get_comments/<slug:slug>/<slug:content_type>/",
        comments.get_comments,
        name="get_comment",
    ),
]
