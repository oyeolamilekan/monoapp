from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class TagsField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_prep_value(self, value):
        return str(value).lower()
    
class Catergories(models.Model):
    '''
        Parent Catergories for shop owners
    '''

    title = models.CharField(max_length=200)
    objects = models.Manager()
    tags = ArrayField(TagsField(max_length=200))

    def __str__(self):
        return '{title} - {tags}'.format(title=self.title, tags=self.tags)
        