from django.urls import path

from ..views import auth_view

AUTH_URL = [
    # Auth login path
    path('register/', auth_view.RegisterAPI.as_view(), name='register'),
    path('login/', auth_view.LoginAPI.as_view(), name='login'),
    path('change_password/', auth_view.ChangePasswordView.as_view(),
         name="change_password"),
]
