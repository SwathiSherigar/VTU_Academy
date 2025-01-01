# Generated by Django 5.1.4 on 2024-12-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0003_remove_videolecture_semester_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="videonote",
            name="branch",
        ),
        migrations.AddField(
            model_name="videonote",
            name="semester",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="videonote",
            name="year",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="videonote",
            name="notes_image",
            field=models.ImageField(blank=True, null=True, upload_to="notes/"),
        ),
        migrations.AlterField(
            model_name="videonote",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="videonote",
            name="video_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]