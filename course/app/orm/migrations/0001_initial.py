# Generated by Django 4.2.1 on 2023-05-22 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
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
                ("address", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "place",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="orm.place",
                    ),
                ),
                ("serves_hot_dogs", models.BooleanField(default=False)),
                ("serves_pizza", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Waiter",
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
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orm.restaurant"
                    ),
                ),
            ],
        ),
    ]
