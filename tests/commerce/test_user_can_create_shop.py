import json

from django.test import TestCase
from django.urls import reverse

from shop.models import Shop

from ..factories import UserFactory
from ..utils import get_token


class WhenUserCreateShop(TestCase):
    """[Tests when the user tries to create a user]
    
    Arguments:
        TestCase {[type]} -- [Testcase param]
    """

    expected_status_code = 200
    name = "Dangote"
    category = "Automobile"
    phone_number = "08037452103"

    def setUp(self):
        """
            [Set up the data neeeded]
        """
        self.user = UserFactory()
        token = get_token(user=self.user)
        self.auth = "Token {}".format(token)
        payload = {
            "shopName": self.name,
            "shopCategory": self.category,
            "phoneNumber": self.phone_number,
        }
        self.response = self.client.post(
            reverse("api:create_shop"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_status_code(self):
        """
            [Test if the succes code match the one returned]
        """
        assert self.response.status_code == self.expected_status_code

    def test_is_shop_saved(self):
        """
            [Test if the shop has been created]
        """
        if self.expected_status_code == 201:
            assert Shop.objects.filter(title=self.name).exists()
