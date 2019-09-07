import json
from django.test import TestCase
from django.urls import reverse

from feedbacks.models import FeedBacks
from ..factories import UserFactory
from ..utils import get_token


class WhenUserCreatesFeedback(TestCase):
    """
    Test if user can create a feedback

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.data_payload = {
            "score": "great",
            "title": "This is great web app",
            "body": "I love what you have created",
        }
        self.auth = "Token {}".format(get_token(self.user))
        self.response = self.client.post(
            reverse("api:create_feedback"),
            data=json.dumps(self.data_payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_request_status(self):
        """
        Check if the action was successful
        """
        assert self.response.status_code == 201

    def test_feedback_created(self):
        assert FeedBacks.objects.all().count() == 1
