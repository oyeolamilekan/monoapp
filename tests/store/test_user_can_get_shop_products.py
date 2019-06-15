from django.test import TestCase
from django.urls import reverse

from api.serializers.commerce import ProductSerializer

from ..factories import ProductFactory, ShopFactory


class WhenUserGetShopProduct(TestCase):
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
            reverse(
                "api:shop_product",
                kwargs={"slug": self.shop.slug, "cat": self.product.genre["slug"]},
            ),
            content_type="application/json",
        )

    def test_response_code(self):
        """
            [Test if there are no errors]
        """
        assert self.response.status_code == 200

    def test_products_returned(self):
        """
            [Check if the info are returned]
        """
        product = ProductSerializer(self.product)
        assert self.response.json()["results"] == [product.data]
