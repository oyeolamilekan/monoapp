# Generated by Django 2.1.1 on 2019-07-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_analytics_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='url',
            field=models.CharField(blank=True, max_length=800),
        ),
    ]
