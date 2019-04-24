from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from basemodel.base_model import BaseModel

class User(AbstractUser, BaseModel):
    """
        The custom user model
    """

    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=200, null=True)
    is_commerce = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
