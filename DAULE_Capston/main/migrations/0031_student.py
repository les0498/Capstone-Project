# Generated by Django 4.1.7 on 2023-06-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0030_remove_user_q10_remove_user_q8_remove_user_q9"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("studentID", models.IntegerField()),
            ],
        ),
    ]