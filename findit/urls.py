from django.urls import path

from . import views


urlpatterns = [
    path('longcr/',views.index),
    path('j_g/',views.j_gr),
    path('j_l/',views.j_lr),
    path('j_p/',views.j_pr),
    path('k_g/',views.k_gr),
    path('k_l/',views.k_kl),
    path('k_p/',views.k_pr),
]