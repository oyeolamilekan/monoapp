from django.test import TestCase
from django.urls import reverse

from ..factories import ProductFactory, ShopFactory


class WhenUserCanSearchProduct(TestCase):
    """
        [Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        """
            [Sets up the testing database]
        """
        self.shop = ShopFactory()
        self.product = ProductFactory(shop_rel=self.shop)
        self.response = self.client.get(
            reverse("api:r_search", kwargs={"slug": self.shop.slug}),
            {"q": self.product.name},
            content_type="application/json",
        )

    def test_response_code(self):
        """
            [Test if there are no errors]
        """
        assert self.response.status_code == 200
