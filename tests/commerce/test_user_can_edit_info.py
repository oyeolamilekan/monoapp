import json

from django.test import TestCase
from django.urls import reverse

from shop.models import Shop

from ..factories import ShopFactory, UserFactory
from ..utils import get_token


class WhenUserEditShopInfo(TestCase):
    """
        [Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        self.auth = "Token {}".format(get_token(self.user))
        payload = {
            "address": "25 josphe ogeare road",
            "description": "Nothing to describe about",
            "phoneNumber": "08087307896",
            "logo": "",
        }
        self.response = self.client.put(
            reverse("api:save_info"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_request_status(self):
        assert self.response.status_code == 200

    def test_product_created(self):
        shop = Shop.objects.get(id=self.shop.id)
        assert self.shop.phone_number != shop.phone_number
