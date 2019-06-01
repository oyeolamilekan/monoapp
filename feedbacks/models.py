from django.db import models
from basemodel.base_model import BaseModel
from accounts.models import User
from constants.feedback import Feedback
# Create your models here.


class FeedBacks(BaseModel):
    user = models.ForeignKey(User, on_delete=True, blank=True)
    score = models.CharField(max_length=200, choices=Feedback.FEEDBACK_CHOICES)
    title = models.CharField(max_length=200)
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.score}-{self.title}"
