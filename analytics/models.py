from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.db import models

from basemodel.base_model import BaseModel

# Create your models here.


class Analytics(BaseModel):
    """
    [This database table is meant to store analytical performance,
    of products, promotions, and pages of buisnesses]
    
    Arguments:
        models {[type]} -- [description]
    """
    content_type = models.ForeignKey(ContentType, on_delete=True, blank=True, null=True)
    object_id = models.CharField(max_length=50, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    url = models.CharField(max_length=200, blank=True)
    objects = models.Manager()
    info = JSONField(default=list)

    def __str__(self):
        return "View objects"