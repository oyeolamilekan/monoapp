# Generated by Django 2.1.1 on 2019-07-28 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_auto_20190707_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analytics',
            options={'ordering': ['-created']},
        ),
    ]