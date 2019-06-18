from django.urls import path

from api.views import auth_view

AUTH_URL = [
    # Auth login path
    path("register/", auth_view.RegisterAPI.as_view(), name="register"),
    path("login/", auth_view.LoginAPI.as_view(), name="login"),
    path(
        "change_password/",
        auth_view.ChangePasswordView.as_view(),
        name="change_password",
    ),
    path("reset/", auth_view.create_token, name="reset"),
    path("verify-token/<slug:token>/", auth_view.verify_token, name="verify-token"),
    path("change-password/", auth_view.change_password, name="change-password"),
]
