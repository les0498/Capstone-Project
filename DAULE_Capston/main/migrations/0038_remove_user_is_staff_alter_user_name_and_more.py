# Generated by Django 4.1.7 on 2023-06-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0037_userinfo_remove_user_q1_remove_user_q2_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="is_staff",),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]