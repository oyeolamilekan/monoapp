from django.contrib import admin
from .models import Products, UserPicks

# Register your models here.
admin.site.register(Products)
admin.site.register(UserPicks)