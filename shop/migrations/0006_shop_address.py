# Generated by Django 2.1.7 on 2019-04-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_shop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
