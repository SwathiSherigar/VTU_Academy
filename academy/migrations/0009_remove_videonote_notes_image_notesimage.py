# Generated by Django 5.1.4 on 2025-01-01 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "academy",
            "0008_remove_videonote_notes_images_videonote_notes_image_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="videonote",
            name="notes_image",
        ),
        migrations.CreateModel(
            name="NotesImage",
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
                ("image", models.ImageField(upload_to="notes_images/")),
                (
                    "video_note",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes_images",
                        to="academy.videonote",
                    ),
                ),
            ],
        ),
    ]
