# Generated by Django 2.1.7 on 2019-05-29 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0007_auto_20190523_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='lppo',
        ),
    ]