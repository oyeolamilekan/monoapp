from django.test import TestCase
from django.urls import reverse

from ..factories import UserFactory, ShopFactory


class UserCanLogin(TestCase):
    """
    [This test if the user can login]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory(password="oyeolamilekan")
        self.shop = ShopFactory(user=self.user)
        self.payload = {"email": self.user.email, "password": "oyeolamilekan"}
        self.response = self.client.post(reverse("api:login"), data=self.payload)

    def test_response(self):
        """
            [Test if the status code is the same]
        """
        assert self.response.status_code == 200

    def test_user_name(self):
        """
            [Test if user user name is the same]
        """
        assert self.response.json()["name"] == self.user.name

    def test_user_email(self):
        """
            [Test if user email is the same]
        """
        assert self.response.json()["user"]["email"] == self.user.email
