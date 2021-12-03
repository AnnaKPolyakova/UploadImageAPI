# Generated by Django 3.2.9 on 2021-11-26 23:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import image.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                (
                    "image",
                    models.ImageField(
                        help_text="Загрузите фотографию",
                        upload_to="images/",
                        validators=[image.validators.validate_image],
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор изображения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
    ]
