from django.test import TestCase
from django.urls import reverse

from api.serializers.store import ShopSerializer

from ..factories import ShopFactory, UserFactory


class WhenUserGetShopInfo(TestCase):
    """
        [Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        """
            [Sets up the testing database]
        """
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        self.response = self.client.get(
            reverse("api:shop_info", kwargs={"slug": self.shop.slug}),
            content_type="application/json",
        )

    def test_response_code(self):
        """
            [Test if there are no errors]
        """
        assert self.response.status_code == 200

    def test_info_returned(self):
        """
            [Check if the info are returned]
        """
        shop = ShopSerializer(self.shop)
        assert self.response.json()["shop_info"]["shop_name"] == shop.data["title"]
