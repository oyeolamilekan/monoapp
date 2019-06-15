'''
    [This view handles the authentication part of the app.]
'''

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import serializers
from tests.utils import get_token
from accounts.models import User
from api.serializers.auth import ChangePasswordSerializer, RegisterSerializer, LoginSerializer, UserSerializer
from shop.models import Shop
# Resgister api


class RegisterAPI(generics.GenericAPIView):
    '''[This Class based view handles the registration functionality]

    Arguments:
        generics {[type]} -- [description]

    Returns:
        [JSON] -- [It returns json objects based on the action taking by user]
    '''

    serializer_class = RegisterSerializer

    def post(self, request):
        '''[This method recives the request from the user and processes it]

        Arguments:
            request {[request object]} -- [The request sent by the user]

        Returns:
            [JSON] -- [returns json reponse with the needed crendentials]
        '''

        if len(request.data['password']) <= 5:
            raise serializers.ValidationError({'error_type': "Password too small"})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_token(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "name": user.name,
            "is_admin": user.is_superuser,
            "is_commerce": user.is_commerce,
            "token": token
        })

# Login api


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        '''[summary]

        Arguments:
            request {[type]} -- [description]

        Returns:
            [type] -- [description]
        '''

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = get_token(user=user)
        try:
            shop_obj = Shop.objects.get(user=user)
        except shop_obj.DoesNotExist:
            shop_obj = ''
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "name": user.name,
            "is_admin": user.is_superuser,
            "is_commerce": user.is_commerce,
            "token": token,
            "shop_name": shop_obj.title if shop_obj else '',
            "shop_slug": shop_obj.slug,
            "shop_logo": shop_obj.logo.url if shop_obj.logo else '',
        })


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


