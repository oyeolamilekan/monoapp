import json

from django.test import TestCase
from django.urls import reverse


class UserCanSignUp(TestCase):
    """
    [This test if the user can login]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.payload = {
            "name": "oye olalekan",
            "email": "john@we.com",
            "is_commerce": True,
            "password": "oyeolami",
        }
        self.response = self.client.post(
            reverse("api:register"),
            data=json.dumps(self.payload),
            content_type="application/json",
        )

    def test_response(self):
        """
            [Test if the status code is the same]
        """
        assert self.response.status_code == 200

    def test_user_name(self):
        """
            [Test if user user name is the same]
        """
        assert self.response.json()["name"] == self.payload["name"]

    def test_user_email(self):
        """
            [Test if user email is the same]
        """
        assert self.response.json()["user"]["email"] == self.payload["email"]
