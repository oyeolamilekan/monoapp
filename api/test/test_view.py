import json

from algoliasearch_django import raw_search
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import pagination, status
from rest_framework.test import APIRequestFactory

from findit.models import Products

from ..serializers import ProductSerializer
from ..views import StandardResultsSetPagination

client = Client()


class GetListProduct(TestCase):
    """ Test A.P.I view for product viewset """

    def setUp(self):
        Products.objects.create(
            name="Samsung note 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('api:products'))
        # get data from db
        product = Products.objects.order_by('?')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductGames(TestCase):
    """ Test A.P.I view for games viewset """

    def setUp(self):
        Products.objects.create(
            name="Ps 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

    def test_get_all_gaming(self):
        # get API response
        response = client.get(reverse('api:gaming'))
        # get data from db
        product = Products.objects.filter(genre='gaming').order_by('?')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductPhones(TestCase):
    """ Test A.P.I view for phones viewset """

    def setUp(self):
        Products.objects.create(
            name="Samsung note 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

    def test_get_all_phones(self):
        print('hello world')
        # get API response
        response = client.get(reverse('api:phone'))
        # get data from db
        product = Products.objects.filter(genre='phone').order_by('?')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductLaptops(TestCase):
    """ Test A.P.I view for laptops viewset """

    def setUp(self):
        Products.objects.create(
            name="hp 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="Ps 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="Ps 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="Ps 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="Ps 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

    def test_get_all_laptops(self):
        # get API response
        response = client.get(reverse('api:laptops'))
        # get data from db
        product = Products.objects.filter(genre='laptops').order_by('?')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductForTrendingPhones(TestCase):
    """ Test A.P.I view for trending phones viewset """

    def setUp(self):
        Products.objects.create(
            name="Samsung note 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

        Products.objects.create(
            name="Samsung note 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

    def test_get_all_t_phones(self):
        # get API response
        response = client.get(reverse('api:phone_t'))
        # get data from db
        product = Products.objects.filter(
            genre='phone').order_by('-num_of_clicks')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductForTrendingLaptops(TestCase):
    """ Test A.P.I view for trending laptops viewset """

    def setUp(self):
        Products.objects.create(
            name="hp 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="hp 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="hp 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="hp 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

        Products.objects.create(
            name="hp 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="laptops"
        )

    def test_get_all_t_laptops(self):
        # get API response
        response = client.get(reverse('api:laptops_t'))
        # get data from db
        product = Products.objects.filter(
            genre='laptops').order_by('-num_of_clicks')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductForTrendingGaming(TestCase):
    """ Test A.P.I view for trending gaming viewset """

    def setUp(self):
        Products.objects.create(
            name="Ps 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="gaming"
        )

    def test_get_all_t_laptops(self):
        # get API response
        response = client.get(reverse('api:gaming_t'))
        # get data from db
        product = Products.objects.filter(
            genre='gaming').order_by('-num_of_clicks')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetListProductForShop(TestCase):
    """ Test A.P.I view for trending gaming viewset """

    def setUp(self):
        Products.objects.create(
            name="Ps 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

    def test_get_all_shop_p(self):
        # get API response
        response = client.get(reverse('api:q_shop', kwargs={
                              'slug': 'jumia', 'cat': 'gaming'}))
        # get data from db
        product = Products.objects.filter(
            shop='jumia').order_by('-num_of_clicks')
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewFeedBack(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'score': 'Very Good',
            'email': 'johnsonon@gmail.com',
            'message': 'Pamerion',
        }
        self.invalid_payload = {
            'score': '',
            'email': 4,
            'message': 'Pamerion',
        }

    def test_create_valid_feedback(self):
        response = client.post(
            reverse('api:feedback'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_feedback(self):
        response = client.post(
            reverse('api:feedback'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetListProductForSearch(TestCase):
    """ Test A.P.I view for search viewset """

    def setUp(self):
        Products.objects.create(
            name="Ps 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

    def test_get_all_search(self):
        # get API response
        response = client.get(reverse('api:r_search'), {'q': 'Ps'})
        # get data from db
        params = {"hitsPerPage": 15}
        queryset = raw_search(Products, 'Ps', params)
        self.assertEqual(response.json()['results'], queryset['hits'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RedirectClicks(TestCase):
    """ Test A.P.I view for redirect viewset """

    def setUp(self):
        Products.objects.create(
            name="Ps 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 2", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 3", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 1", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

        Products.objects.create(
            name="Ps 9", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="jumia", genre="gaming"
        )

    def test_redirect(self):
        # get API response
        response = client.get(reverse('api:r_redirect', kwargs={'id': 2}))
        # get data from db
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class CreateShoppingGTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="olamilekan", password="oyeolamilekan", email="johns@er.com")
        self.valid_payload = {
            'user': 'olamilekan',
            'article': 'cloth',
        }
        self.invalid_payload = {
            'user': '',
            'article': 'cloth',
        }

    def test_create_valid_shopping_cat(self):
        response = client.post(
            reverse('api:catergory'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_shopping_cat(self):
        response = client.post(
            reverse('api:catergory'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetUserTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="olamilekan", password="oyeolamilekan", email="johns@er.com")
        self.valid_payload = {
            'user': 'olamilekan',
        }
        self.invalid_payload = {
            'user': '',
        }

    def test_create_valid_user_choice(self):
        response = client.get(
            reverse('api:list'),
            self.valid_payload,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_user_choice(self):
        response = client.get(
            reverse('api:catergory'),
            self.invalid_payload,
        )
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class GetUserProductsTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="olamilekan", password="oyeolamilekan", email="johns@er.com")
        self.header = {
            'HTTP_AUTHORIZATION': 'olamilekan',
        }
        self.invalid_header = {
            'HTTP_AUTHORIZATION': '',
        }

    def test_create_valid_user_choice(self):
        response = client.get(
            reverse('api:product_list'),
            **self.header,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_user_choice(self):
        response = client.get(
            reverse('api:product_list'),
            **self.invalid_header,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
