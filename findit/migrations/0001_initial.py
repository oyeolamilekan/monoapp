# Generated by Django 2.1.7 on 2019-03-16 19:03

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
            name='Products',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
                ('converted_price', models.CharField(blank=True, max_length=300, null=True)),
                ('real_price', models.IntegerField(default=0)),
                ('real_price_2', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='')),
                ('source_url', models.CharField(max_length=700)),
                ('shop', models.CharField(max_length=300)),
                ('num_of_clicks', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('old_price', models.CharField(blank=True, max_length=200, null=True)),
                ('old_price_2', models.CharField(blank=True, max_length=200, null=True)),
                ('old_price_digit', models.IntegerField(default=0)),
                ('old_price_digit_2', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('sub_genre', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('genre', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('lppo', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='UserPicks',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('picks', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserPicks',
                'verbose_name_plural': 'UserPicks',
                'ordering': ['-created'],
            },
        ),
    ]
