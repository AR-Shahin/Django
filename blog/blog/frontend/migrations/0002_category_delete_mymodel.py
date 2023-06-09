# Generated by Django 4.2 on 2023-04-21 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("status", models.BooleanField(default=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="MyModel",
        ),
    ]
