# Generated by Django 2.1.7 on 2019-05-20 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190517_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='categories',
        ),
    ]