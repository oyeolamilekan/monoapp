# Generated by Django 2.1.7 on 2019-05-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190523_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='phone_number',
            field=models.CharField(default='', max_length=300),
        ),
    ]
