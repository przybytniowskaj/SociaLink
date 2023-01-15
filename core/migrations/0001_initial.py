# Generated by Django 4.1.3 on 2022-12-25 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("id_user", models.IntegerField()),
                ("bio", models.TextField(blank=True)),
                (
                    "profile_img",
                    models.ImageField(
                        default="default_photo.png", upload_to="profile_photos"
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=20)),
                ("surname", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=15)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
