from django.test import TestCase
from findit.models import Products


class ProductTest(TestCase):
    """ Test module for Product """

    def setUp(self):
        Products.objects.create(
            name="Samsung note 4", price='20333', source_url="https://realpython.com/test-driven-development-of-a-django-restful-api/", shop="Jumia", genre="phone"
        )

    def test_product_details(self):
        response = Products.objects.get(name="Samsung note 4")
        self.assertEqual(
            response.get_product_description(), "Samsung note 4 belongs to phone category."
        )
