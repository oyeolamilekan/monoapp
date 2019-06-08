from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from basemodel.base_model import BaseModel
from comment.models import Comment
from constants.lesson import Lessons

# Create your models here.


class Lesson(BaseModel):
    """
    [This model handles the tuts uploaded for teaching our users how to use the service]

    Arguments:
        BaseModel {[ Models ]} -- [ It inherits from basemodel class ]

    """
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=300, choices=Lessons.LESSON_CHOICES)
    objects = models.Manager()
    video_url = models.CharField(max_length=300)
    comments = GenericRelation(Comment)

    def __str__(self):
        return f'{self.title} {self.video_url}'
