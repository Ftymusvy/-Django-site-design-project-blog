# Generated by Django 5.0.4 on 2024-07-16 22:53

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bloggers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("comments_count", models.IntegerField(default=0)),
                ("likes_count", models.IntegerField(default=0)),
                (
                    "post_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("is_published", models.BooleanField(default=True)),
                ("photo_main", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                (
                    "photo_1",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_2",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_3",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_4",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_5",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_6",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "blogger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="bloggers.blogger",
                    ),
                ),
            ],
        ),
    ]
