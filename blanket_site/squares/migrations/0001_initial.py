# Generated by Django 5.0.1 on 2024-02-01 16:20

import contributors.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contributors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Square",
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
                ("name", models.CharField(max_length=256)),
                ("image", models.ImageField(upload_to="")),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=models.SET(contributors.models.get_anonymous_user),
                        to="contributors.person",
                    ),
                ),
            ],
        ),
    ]
