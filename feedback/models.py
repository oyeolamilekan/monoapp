from django.db import models
from basemodel.base_model import BaseModel
from accounts.models import User
# Create your models here.


class Feedback(BaseModel):
    user = models.ForeignKey(User, on_delete=True, blank=True)
    score = models.CharField(max_length=200)
    objects = models.Manager()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"{self.score}-{self.title}"
