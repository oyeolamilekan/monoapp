# Generated by Django 2.1.7 on 2019-06-08 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0009_auto_20190608_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
    ]