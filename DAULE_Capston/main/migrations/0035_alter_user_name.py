# Generated by Django 4.1.7 on 2023-06-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0034_user_is_active_user_is_admin_user_is_staff_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]