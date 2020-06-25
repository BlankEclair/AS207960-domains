# Generated by Django 3.0.7 on 2020-06-24 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domains', '0024_auto_20200624_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='HangoutsUserLinkState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('return_url', models.URLField()),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HangoutsUsers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
