import json
import tempfile

from django.core.files import File
from django.test import TestCase
from django.urls import reverse
from PIL import Image

from findit.models import Products

from ..factories import ShopFactory, UserFactory
from ..utils import get_token


class WhenUserCreateProduct(TestCase):
    """
        [ Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.shop = ShopFactory(user=self.user)
        self.auth = "Token {}".format(get_token(self.user))
        self.filename = "iphone"
        self.file = File(open("imgs/iphone12.jpg", "rb"))
        image = Image.new("RGB", (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix=".png")
        image.save(tmp_file)
        payload = {
            "productName": "iphone 8",
            "productPrice": "20000",
            "description": "this is a great device",
            "tags": json.dumps(self.shop.categories[0]),
            "file": tmp_file.name,
        }
        self.response = self.client.post(
            reverse("api:create_product"),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_request_status(self):
        assert self.response.status_code == 201

    def test_product_created(self):
        assert Products.objects.filter(shop_rel=self.shop).count() == 1

