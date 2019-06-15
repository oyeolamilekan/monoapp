from django.test import TestCase
from django.urls import reverse

from api.serializers.store import ShopSerializer

from ..factories import ShopFactory, UserFactory
from ..utils import get_token


class WhenUserGetShopInfo(TestCase):
    """
        [ Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        token = get_token(user=self.user)
        self.auth = "Token {}".format(token)
        self.response = self.client.get(
            reverse("api:get_info"),
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
            [Check if the info are returned]
        """
        shop = ShopSerializer(self.shop)
        assert self.response.json() == shop.data
