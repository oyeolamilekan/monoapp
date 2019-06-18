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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ResetToken(BaseModel):
    """
    
    This is models that creates token for the user,
    if they have requested for a password reset

    """

    user = models.ForeignKey(User, on_delete=True)
    token = models.CharField(max_length=200)
    expiry = models.DateField(auto_now_add=True)
    used = models.BooleanField(default=False)
    objects = models.Manager()
    def __str__(self):
        return f'{self.user} - {self.token}'
