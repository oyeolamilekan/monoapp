from django.conf import settings
from django.db import models

from accounts.models import User
from basemodel.base_model import BaseModel
from shop.models import Shop
from django.contrib.postgres.fields import JSONField

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
        max_length=200, blank=True, null=True, default='')
    genre = JSONField(default=dict)

    # Returns the name of the product
    def __str__(self):
        return f'{self.name} {self.shop_slug}'

    # Return a simple descriptions of the object
    def get_product_description(self):
        return self.name + ' belongs to category.'

    # Again Does something's i don't undetstand
    # Orders by an id
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'