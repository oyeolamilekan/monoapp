# Generated by Django 2.1.1 on 2019-08-05 11:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allies',
            name='user',
            field=models.ForeignKey(null=True, on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
