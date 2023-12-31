# Generated by Django 4.2.5 on 2023-11-17 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("fbapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="comment",
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
                ("comment_id", models.UUIDField(verbose_name=uuid.uuid4)),
                ("text", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="feeds",
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
                ("feed_id", models.UUIDField(verbose_name=uuid.uuid4)),
                ("image", models.ImageField(upload_to="feed")),
                ("desc", models.CharField(max_length=100)),
                ("date_feeded", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="like",
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
                ("liked", models.BooleanField(default=False)),
                (
                    "feed_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feed",
                        to="fbapp.feeds",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="like",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="profile",
        ),
        migrations.AddField(
            model_name="comment",
            name="feed_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fbapp.feeds"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
