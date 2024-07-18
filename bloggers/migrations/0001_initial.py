# Generated by Django 5.0.4 on 2024-07-16 22:53

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("photo", models.ImageField(upload_to="photos/bloggers/%Y/%m/%d/")),
                (
                    "birth_date",
                    models.DateField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "register_date",
                    models.DateField(blank=True, default=datetime.datetime.now),
                ),
                ("posts_count", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(
                        default=0,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]