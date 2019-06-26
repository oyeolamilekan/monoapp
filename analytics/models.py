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
    content_type = models.ForeignKey(ContentType, on_delete=True)
    object_id = models.CharField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')
    view_count = models.IntegerField(default=1)
    click_count = models.IntegerField(default=1)
    objects = models.Manager()
    info = JSONField(default=list)

    def __str__(self):
        return "view count: {} -  clicked count: {}".format(self.view_count, self.click_count)
