from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import JSONField
from django.db import models

from basemodel.base_model import BaseModel
from shop.models import Shop
from analytics.models import Analytics
# Create your models here.


class ProductList(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created')


class Products(BaseModel):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    objects = ProductList()
    image = models.ImageField()
    source_url = models.CharField(max_length=700, blank=True)
    shop_rel = models.ForeignKey(Shop, null=True, on_delete=True)
    num_of_clicks = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    shop_slug = models.CharField(
        max_length=250, blank=True, null=True, default='')
    genre = JSONField(default=dict)
    analytics = GenericRelation(Analytics)

    # Returns the name of the product
    def __str__(self):
        return f'{self.name} {self.shop_slug}'

    # Return a simple descriptions of the object
    def get_product_description(self):
        return self.name + ' belongs to category.'
    
    def get_product_name(self):
        return self.name
    
    def get_product_id(self):
        return self.id

    # Again Does something's i don't undetstand
    # Orders by an id
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
