# from algoliasearch_django import raw_search
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import redirect
# from rest_framework import pagination, status, viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from accounts.models import User
# from findit.models import Products, UserPicks
# from api.serializers.commerce import ProductSerializer


# class StandardResultsSetPagination(pagination.PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


# class ProductView(viewsets.ModelViewSet):
#     queryset = Products.objects.order_by('?')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination


# class GameProductView(viewsets.ModelViewSet):
#     queryset = Products.objects.filter(genre='gaming').order_by('?')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination


# class ProductViewPhone(viewsets.ModelViewSet):
#     queryset = Products.objects.filter(genre='phone').order_by('?')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination


# class ProductViewLaptop(viewsets.ModelViewSet):
#     queryset = Products.objects.filter(genre='laptops').order_by('?')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination


# class ProductViewLaptops(viewsets.ModelViewSet):
#     queryset = Products.objects.filter(
#         genre='laptops').order_by('-num_of_clicks')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination


# class ProductViewPhones(viewsets.ModelViewSet):
#     queryset = Products.objects.filter(
#         genre='phone').order_by('-num_of_clicks')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination


# class ProductViewGaming(viewsets.ModelViewSet):
#     queryset = Products.objects.filter(
#         genre='gaming').order_by('-num_of_clicks')
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination

# # Allows me to filter dynamically
# # it's filters both catergory
# # and the shop so its a 2 in 1
# # Through the shops without
# # Having to write multiple code


# @api_view(['GET'])
# def ShopProduct(request, slug, cat):
#     if cat == 'all':
#         products = Products.objects.filter(shop=slug)
#     else:
#         products = Products.objects.filter(shop=slug, genre=cat)
#     paginator = pagination.PageNumberPagination()
#     paginator.page_size = 10
#     result_page = paginator.paginate_queryset(products, request=request)
#     serializer = ProductSerializer(result_page, many=True)
#     return paginator.get_paginated_response(serializer.data)


# @api_view(['POST'])
# def feedback(request):
#     # serailizer = FeedbackSerializer(data=request.data)
#     # if serailizer.is_valid():
#     #     serailizer.save()
#     #     return Response(serailizer.data, status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_400_BAD_REQUEST)




def search_query(request,slug):
    try:
        queryset = Products.objects.all()
        query = request.GET.get('q')
        if query:
            params = {"hitsPerPage": 15}
            queryset = raw_search(Products, query, params)
        return JsonResponse({'results': queryset['hits']})
    except queryset.DoesNotExist:
        return HttpResponse('nothing')


# def number_of_clicks(request, id):
#     if Products.objects.filter(id=id).exists():
#         product = Products.objects.get(id=id)
#         product.num_of_clicks = product.num_of_clicks + 1
#         product.save()
#         if product.shop == 'jumia':
#             return redirect(
#                 f'http://c.jumia.io/?a=35588&c=11&p=r&E=kkYNyk2M4sk%3d&ckmrdr={product.source_url}&utm_source=cake&utm_medium=affiliation&utm_campaign=35588&utm_term=')
#         else:
#             return redirect(product.source_url)
#     else:
#         return HttpResponse('Not Found on this beautiful server')


# @api_view(['POST'])
# def create_genre(request):
#     try:
#         user = request.data['user']
#         product = request.data['article'].lower()
#         user = User.objects.get(username=user)
#         if not UserPicks.objects.filter(user=user, picks=product).exists():
#             user_p = UserPicks(user=user, picks=product)
#             user_p.save()
#             return Response(data={'resp': 'ok'}, status=status.HTTP_201_CREATED)
#         else:
#             user_p = UserPicks.objects.get(user=user, picks=product)
#             user_p.delete()
#             return Response(data={'resp': 'not ok'}, status=status.HTTP_201_CREATED)
#     except:
#         return Response(data={'resp': 'broken'}, status=status.HTTP_400_BAD_REQUEST)

# # Get the user product category
# # The returns the one


# @api_view(['GET'])
# def get_user_choice(request):
#     user = request.GET.get('user')
#     user = User.objects.get(username=user)
#     user_picks = UserPicks.objects.filter(user=user)
#     user_num = len(user_picks)
#     list_p = [user_p.picks.lower() for user_p in user_picks]
#     return Response(data={'res': list_p, 'user_num': user_num}, status=status.HTTP_200_OK)


# #
# @api_view(['GET'])
# def get_user_products(request):
#     '''
#     This request is in function based
#     Why because it requires some simple
#     Auth customization
#     It uses a get request because the user
#     is requesting some data from the server
    
#     Arguments:
#         request {[request object]} -- [request object to check authorization]
    
#     Returns:
#         [JSON] -- [returns response in json objects]
#     '''

#     try:
#         user = request.META['HTTP_AUTHORIZATION']
#         user = User.objects.get(email=user)
#         user_picks = UserPicks.objects.filter(user=user)
#         list_c = [user_p.picks.lower() for user_p in user_picks]
#         user_prod = Products.objects.filter(genre__in=list_c).order_by('?')
#         paginator = pagination.PageNumberPagination()
#         paginator.page_size = 10
#         result_page = paginator.paginate_queryset(user_prod, request=request)
#         serializer = ProductSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)
#     except:
#         import traceback
#         traceback.print_exc()
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# ## New View Api for Aliexpress ##
# ## Saw something fun on producthunt ##
