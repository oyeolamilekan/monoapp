from django.test import TestCase
from django.urls import reverse

from lessons.models import Lesson

from ..factories import CommentsFactory, LessonFactory, UserFactory
from ..utils import get_token


class WhenUserGetLessons(TestCase):
    """
        [Test if user can get products]

    Arguments:
        TestCase {[type]} -- [description]
    """

    def setUp(self):
        self.user = UserFactory()
        self.lesson = LessonFactory()
        self.comments = CommentsFactory(content_object=self.lesson, user=self.user)
        token = get_token(user=self.user)
        self.auth = "Token {}".format(token)
        self.response = self.client.get(
            reverse(
                "api:get_comment",
                kwargs={"slug": self.lesson.id, "content_type": "lessons"},
            ),
            HTTP_AUTHORIZATION=self.auth,
            content_type="application/json",
        )

    def test_response_code(self):
        """
            [Test if there are no errors]
        """
        assert self.response.status_code == 200

    def test_lesson_returned(self):
        """
            [Check if the products are created]
        """
        lesson = Lesson.objects.get(id=self.lesson.id)
        assert lesson.comments.all().count() == 1
