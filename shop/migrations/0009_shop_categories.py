# Generated by Django 2.1.7 on 2019-05-20 18:45

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_shop_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='categories',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
