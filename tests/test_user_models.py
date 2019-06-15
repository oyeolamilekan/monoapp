# tests/test_models.py
from django.test import TestCase

from .factories import UserFactory


class UserTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        user = UserFactory()
        self.assertEqual(str(user), user.email)
