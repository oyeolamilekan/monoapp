from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import pagination, status, viewsets, generics
from findit.models import Products
from api.serializers import ProductSerializer, CatergoriesSerializer, ShopSerializer
from shop.models import Shop
from tags.models import Catergories


@api_view(['POST'])
def create_shop(request):
    '''
    Creates a shop for the user

    Arguments:,
        request {[request object]} -- [the neccessary data needed to create a shop]

    Returns:
        [JSON] -- [returns json if its is successful or not]
    '''

    shop = Shop.objects.filter(
        title=request.data['shopName'])
    if shop.exists():
        return Response({
            'is_exist': True,
            'msg': 'This shop already exist'
        })
    shop = Shop.objects.create(
        title=request.data['shopName'],
        user=request.user)
    shop.save()
    return Response({
        'is_exist': False,
        'msg': 'Success.'
    })


@api_view(['GET'])
def shop_products(request):
    '''Get the products assiociated with this user shop.

    Arguments:
        request {[request object]} -- [Used as a form of verification of a user authencity]
    '''

    shop = Shop.objects.get(user=request.user)
    products = Products.objects.filter(shop_rel=shop)
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(products, request=request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def create_product(request):
    shop_obj = Shop.objects.get(user=request.user)
    data_payload = {
        'name': request.data['productName'],
        'price': request.data['productPrice'],
        'description': request.data['description'],
        'genre': request.data['tags'],
        'image': request.data['file'],
        'shop_rel': shop_obj
    }
    products = Products.objects.create(**data_payload)
    products.save()
    products_serailzer = ProductSerializer(products)
    return Response(data={'product': products_serailzer.data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_tags(request):
    shop = Shop.objects.get(user=request.user)
    shop.categories = request.data
    shop.save()
    return Response(status=status.HTTP_201_CREATED)


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CatergoriesView(viewsets.ModelViewSet):
    queryset = Catergories.objects.order_by('?')
    serializer_class = CatergoriesSerializer
    pagination_class = StandardResultsSetPagination


@api_view(['GET'])
def get_catergories(request):
    catergory = Catergories.objects.order_by('?')
    choosen_catergory = Shop.objects.get(user=request.user)
    choosen_list = choosen_catergory.categories
    catergory_serializer = CatergoriesSerializer(catergory, many=True)
    return Response(data={'choosen_catergory': choosen_list, 'catergory_serializer': catergory_serializer.data}, status=status.HTTP_200_OK)


class EditShopInfo(generics.GenericAPIView):
    '''[summary]

    Arguments:
        generics {[ Rest Api Object ]} -- [description]
    '''

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):

        queryset = self.get_queryset().filter(title=kwargs.get('slug'))
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_info(request):
    user_info = Shop.objects.get(user=request.user)
    serializer = ShopSerializer(user_info)
    return Response(serializer.data)


@api_view(['POST'])
def save_info(request):
    user_info_obj = Shop.objects.get(user=request.user)
    user_info_obj.address = request.data['address']
    user_info_obj.description = request.data['description']
    if request.data['logo']:
        user_info_obj.logo = request.data['logo']
    user_info_obj.save()
    return Response(status=status.HTTP_200_OK)
