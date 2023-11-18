# Generated by Django 4.2.5 on 2023-11-18 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("fbapp", "0011_rename_like_like_msg"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="like_msg",
            name="feedid",
        ),
        migrations.AddField(
            model_name="like_msg",
            name="feed_id",
            field=models.CharField(default=uuid.uuid4, max_length=1000),
        ),
    ]
