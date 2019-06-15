import random
import uuid

from django.utils.text import slugify
from factory import DjangoModelFactory, Faker, SubFactory, PostGenerationMethodCall
from accounts.models import User
from findit.models import Products
from shop.models import Shop
from lessons.models import Lesson


class UserFactory(DjangoModelFactory):
    name = Faker('name')
    email = Faker('email')
    password = PostGenerationMethodCall("set_password", "password")
    is_commerce = True
    id = str(uuid.uuid1())

    class Meta:
        model = User


class ShopFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    title = Faker('name')
    category = 'Automobile'
    slug = slugify(title)
    address = Faker('name')
    phone_number = '08037452103'
    description = Faker('text')
    categories = random.choice([[{"name": "nnnn jkj", "slug": "nnnn-jkj", "public_slug": "nnnn-jkj"}],
                                [{"name": "phones", "slug": "phones", "public_slug": "phones"}]])
    id = str(uuid.uuid1())
    

    class Meta:
        model = Shop

class ProductFactory(DjangoModelFactory):
    name = Faker('name')
    price = random.randint(1000, 20000)
    shop_rel = SubFactory(ShopFactory)
    description = Faker('text')
    genre = {"name": "nnnn jkj", "slug": "nnnn-jkj", "public_slug": "nnnn-jkj"}
    id = str(uuid.uuid1())


    class Meta:
        model = Products

class LessonFactory(DjangoModelFactory):
    title = Faker('name')
    category = 'setting_up'
    video_url = 'http://video.com/nfWdnnd2'

    class Meta:
        model = Lesson