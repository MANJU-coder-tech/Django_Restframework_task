# Generated by Django 4.1.7 on 2023-03-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="adding",
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
                ("number_1", models.IntegerField()),
                ("number_2", models.IntegerField()),
            ],
        ),
    ]
