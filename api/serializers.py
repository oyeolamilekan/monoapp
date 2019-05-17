from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from accounts.models import User
from findit.models import Products
from shop.models import Shop
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

# Create a serializer


class ShopCreateSerializer(serializers.Serializer):
    shop = serializers.CharField()

    def validate_shop(self, data):
        return True
        print(data, 'jjj')

# Shop Api


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'user', 'slug', 'title', 'categories',
                  'address', 'description', 'logo')

# User Serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

# Catergory serializer


class CatergoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catergories
        fields = ('id', 'title', 'tags')


# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Crendentials')


# Register Serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'is_commerce', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_commerce=validated_data['is_commerce'])
        return user

# Change password functionality


class ChangePasswordSerializer(serializers.Serializer):

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)