from django.test import TestCase
from django.urls import reverse

from findit.models import Products

from ..factories import ProductFactory, UserFactory, ShopFactory
from ..utils import get_token


class WhenUserGetRelatedProducts(TestCase):
    """
        [ Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        self.products = ProductFactory(shop_rel=self.shop)
        token = get_token(user=self.user)
        self.auth = "Token {}".format(token)
        self.response = self.client.get(
            reverse("api:shop_products"),
            HTTP_AUTHORIZATION=self.auth,
            content_type="application/json",
        )

    def test_response_code(self):
        """
            [Test if there are no errors]
        """
        assert self.response.status_code == 200

    def test_products_returned(self):
        """
            [Check if the products are created]
        """
        assert Products.objects.filter(shop_rel=self.shop).count() == 1
