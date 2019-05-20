from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from accounts.models import User
from findit.models import Products
from tags.models import Catergories
User = get_user_model()


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'image', 'source_url',
                  'genre', 'shop', 'price', 'slug', 'description')
    

# Catergory serializer


class CatergoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catergories
        fields = ('id', 'title', 'tags')
