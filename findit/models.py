from accounts.models import User
from django.conf import settings
from django.db import models
from basemodel.base_model import BaseModel
from shop.models import Shop
# Create your models here.


class ProductList(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created')



class Products(BaseModel):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    converted_price = models.CharField(max_length=300, blank=True, null=True)
    real_price = models.IntegerField(default=0)
    objects = ProductList()
    real_price_2 = models.IntegerField(default=0)
    image = models.ImageField()
    source_url = models.CharField(max_length=700, blank=True)
    shop_rel = models.ForeignKey(Shop, null=True, on_delete=True)
    shop = models.CharField(max_length=300)
    num_of_clicks = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    createdate = models.DateTimeField(auto_now_add=True)
    old_price = models.CharField(max_length=200, blank=True, null=True)
    old_price_2 = models.CharField(max_length=200, blank=True, null=True)
    old_price_digit = models.IntegerField(default=0)
    old_price_digit_2 = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True, null=True)
    sub_genre = models.CharField(
        max_length=200, blank=True, null=True, default='')
    genre = models.CharField(max_length=200, blank=True, null=True, default='')
    lppo = models.CharField(max_length=200, blank=True, null=True)

    # Returns the name of the product
    def __str__(self):
        return self.name

    # Return a simple descriptions of the object
    def get_product_description(self):
        return self.name + ' belongs to ' + self.genre + ' category.'

    # Again Does something's i don't undetstand
    # Orders by an id
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


class UserPicks(BaseModel):
    user = models.ForeignKey(User, on_delete=True)
    picks = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user} - {self.picks}'

    class Meta:
        ordering = ['-created']
        verbose_name = 'UserPicks'
        verbose_name_plural = 'UserPicks'
