# Generated by Django 2.1.1 on 2019-06-17 06:25

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190316_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetToken',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('token', models.CharField(max_length=200)),
                ('expiry', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
