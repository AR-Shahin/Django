# Generated by Django 4.2.1 on 2023-05-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_alter_user_options_alter_user_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
