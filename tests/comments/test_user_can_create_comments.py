import json

from django.test import TestCase
from django.urls import reverse

from lessons.models import Lesson
from ..factories import LessonFactory, UserFactory
from ..utils import get_token


class WhenUserCreateComments(TestCase):
    """
        [ Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.lesson = LessonFactory()
        self.auth = "Token {}".format(get_token(self.user))
        payload = {"textbox_value": "iphone 8"}
        self.response = self.client.post(
            reverse(
                "api:create_comments",
                kwargs={"slug": self.lesson.id, "content_type": "lessons"},
            ),
            data=json.dumps(payload),
            content_type="application/json",
            HTTP_AUTHORIZATION=self.auth,
        )

    def test_request_status(self):
        assert self.response.status_code == 200

    def test_comments_created(self):
        lesson = Lesson.objects.get(id=self.lesson.id)
        assert lesson.comments.all().count() == 1

