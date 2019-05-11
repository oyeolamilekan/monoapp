# Generated by Django 2.1.7 on 2019-05-08 23:20

import django.contrib.postgres.fields
from django.db import migrations
import tags.models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catergories',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=tags.models.TagsField(max_length=200), size=None),
        ),
    ]