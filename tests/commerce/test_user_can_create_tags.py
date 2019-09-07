import json

from django.test import TestCase
from django.urls import reverse

from ..factories import ShopFactory
from ..utils import get_token


class WhenUserCreateShopTags(TestCase):
    def setUp(self):
        self.shops = ShopFactory()
        token = get_token(self.shops.user)
        self.auth = "Token {}".format(token)
        payload = {"categoryName": "facebook label"}
        self.response = self.client.post(
            reverse("api:create_tags"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_status_code(self):
        """
            checks the status code
        """
        assert self.response.status_code == 201
