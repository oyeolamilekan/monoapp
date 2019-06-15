import json

from django.test import TestCase
from django.urls import reverse

from findit.models import Products

from ..factories import ShopFactory, UserFactory, ProductFactory
from ..utils import get_token


class WhenUserEditProduct(TestCase):
    """
        [Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        self.products = ProductFactory(shop_rel=self.shop)
        self.auth = "Token {}".format(get_token(self.user))
        payload = {
            "id": str(self.products.id),
            "productName": "Samsung s9 plus",
            "productPrice": "34,300",
            "description": self.products.description,
            "tags": json.dumps(self.products.genre),
            "file": "",
        }
        self.response = self.client.put(
            reverse("api:edit_produts"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_request_status(self):
        assert self.response.status_code == 201

    def test_product_created(self):
        product = Products.objects.get(id=self.products.id)
        assert self.products.name != product.name
