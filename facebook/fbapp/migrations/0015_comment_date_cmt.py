# Generated by Django 4.2.5 on 2023-11-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fbapp", "0014_remove_comment_id_alter_comment_comment_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="date_cmt",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]