# Generated by Django 2.1.7 on 2019-05-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_shop_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.CharField(default='', max_length=300),
        ),
    ]
