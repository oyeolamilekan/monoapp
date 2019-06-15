# tests/test_models.py
import json

from django.test import TestCase
from django.urls import reverse

from ..factories import UserFactory
from ..utils import get_token


class UserChangePassword(TestCase):
    def setUp(self):
        self.user = UserFactory(password="oyeolamilekan")
        token = get_token(user=self.user)
        self.auth = "Token {}".format(token)
        payload = {"old_password": "oyeolamilekan", "new_password": "oyejohnson"}
        self.response = self.client.put(
            reverse("api:change_password"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_status_code(self):
        """
            [Test if the request is successfull]
        """
        assert self.response.status_code == 200
