from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import User
from basemodel.base_model import BaseModel

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=True, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=True)
    object_id = models.CharField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(blank=True)
