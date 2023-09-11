# Generated by Django 4.1.7 on 2023-06-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0048_userinfo_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="name",
            field=models.CharField(default="", max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name="userinfo",
            name="phone_number",
            field=models.CharField(default="", max_length=20, unique=True),
        ),
    ]