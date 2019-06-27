from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from accounts.models import User
from analytics.models import Analytics
from findit.models import BaseModel

# Create your models here.


class Shop(BaseModel):
    """[summary]
    
    Arguments:
        BaseModel {[ Inherited from the model ]} -- [the id is included]
    
    Returns:
        [type] -- [description]
    """
    user = models.ForeignKey(User, on_delete=True, null=True)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=300, default='')
    slug = models.SlugField(max_length=40)
    logo = models.ImageField(blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=300, default="")
    description = models.TextField(blank=True)
    categories = JSONField(default=list)
    objects = models.Manager()
    analytics = GenericRelation(Analytics)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{title} - {slug}'.format(title=self.title, slug=self.slug)

# creats a slug url for the section
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title.lower()) 
    if new_slug is not None:
        slug = new_slug
    qs = Shop.objects.filter(slug=slug).order_by("-created")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id[:5])
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Shop)
