# Generated by Django 2.1.1 on 2019-07-07 12:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_shop_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(null=True, on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
