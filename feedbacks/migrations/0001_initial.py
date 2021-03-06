# Generated by Django 2.1.7 on 2019-06-01 18:57

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBacks',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('score', models.CharField(choices=[('great', 'great'), ('okay', 'okay'), ('medium', 'medium'), ('nice', 'nice')], max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('user', models.ForeignKey(blank=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
