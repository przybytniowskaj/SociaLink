# Generated by Django 4.1.3 on 2023-01-05 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_post_title"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="title",),
    ]