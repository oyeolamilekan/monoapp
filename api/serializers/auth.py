from django.contrib.auth import authenticate
from rest_framework.serializers import (CharField, ModelSerializer, Serializer,
                                        ValidationError)

from accounts.models import User


class LoginSerializer(Serializer):
    """
    Converts the django object to a json serializable
    Arguments:
        Serializer {Serializer} -- [description]
    Raises:
        ValidationError: [description]
    
    Returns:
        [type] -- [description]
    """
    email = CharField()
    password = CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError('Incorrect Crendentials')


# Register Serializers
class RegisterSerializer(ModelSerializer):
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


class ChangePasswordSerializer(Serializer):

    """
    Serializer for password change endpoint.
    """
    old_password = CharField(required=True)
    new_password = CharField(required=True)

# User Serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
