# Generated by Django 4.1.7 on 2023-06-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]
