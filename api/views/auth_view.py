'''
    [This view handles the authentication part of the app.]
'''

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from shop.models import Shop
from api.serializers import LoginSerializer, RegisterSerializer, UserSerializer
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

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "name": user.name,
            "is_admin": user.is_superuser,
            "is_commerce": user.is_commerce,
            "token": token.key
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
        token, _ = Token.objects.get_or_create(user=user)
        try:
            shop_obj = Shop.objects.get(user=user)
        except Exception as e: 
            shop_obj = ''
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "name": user.name,
            "is_admin": user.is_superuser,
            "is_commerce": user.is_commerce,
            "token": token.key,
            "shop_name": shop_obj.title if shop_obj else '',
            "shop_logo": shop_obj.logo.url if shop_obj.logo else '',
        })
