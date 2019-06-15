import json

from django.test import TestCase
from django.urls import reverse

from findit.models import Products

from ..factories import ShopFactory, UserFactory, ProductFactory
from ..utils import get_token


class WhenUserDeleteProduct(TestCase):
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
        payload = {"id": str(self.products.id)}
        self.response = self.client.delete(
            reverse("api:delete_products"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_request_status(self):
        assert self.response.status_code == 200

    def test_product_created(self):
        assert Products.objects.filter(shop_rel=self.shop).count() == 0
