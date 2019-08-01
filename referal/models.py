from django.db import models
from django.utils.crypto import get_random_string
from basemodel.base_model import BaseModel
from django.db.models.signals import pre_save
from accounts.models import User

# Create your models here.


class Referal(BaseModel):
    """
    This table is track how many traffic the user has brought in.
    
    Arguments:
        BaseModel {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    user = models.OneToOneField(User, on_delete=True, null=True)
    user_name = models.CharField(max_length=200)
    tracking_id = models.CharField(max_length=200)
    total_traffic = models.IntegerField(default=0)
    objects = models.Manager()
    day_expiry = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.user_name} - {self.user_name} - {self.total_traffic}"

# creats a slug url for the section
def create_tracking_id(instance, new_tracking_id=None):
    tracking_id = get_random_string(length=6) 
    if new_tracking_id is not None:
        tracking_id = new_tracking_id
    qs = Referal.objects.filter(tracking_id=tracking_id).order_by("-created")
    exists = qs.exists()
    if exists:
        new_tracking_id = "%s-%s" %(tracking_id, qs.first().id[:2])
        return create_tracking_id(instance, new_tracking_id=new_tracking_id)
    return tracking_id


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.tracking_id:
        instance.tracking_id = create_tracking_id(instance)

pre_save.connect(pre_save_post_receiver, sender=Referal)

