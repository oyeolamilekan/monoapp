from django.test import TestCase
from django.urls import reverse


from ..factories import UserFactory, ShopFactory
from ..utils import get_token


class WhenUserGetCategory(TestCase):
    """
        [ Test if user can get Category]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        token = get_token(user=self.user)
        self.auth = "Token {}".format(token)
        self.response = self.client.get(
            reverse("api:catergory_list"),
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
            [Check if the tags are created]
        """
        assert self.shop.categories[0] == self.response.json()["shop_categories"][0]
