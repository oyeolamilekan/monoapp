# Generated by Django 2.1.7 on 2019-05-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findit', '0006_products_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='sub_genre',
        ),
        migrations.AddField(
            model_name='products',
            name='shop_slug',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]