from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import User


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

# User Serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')