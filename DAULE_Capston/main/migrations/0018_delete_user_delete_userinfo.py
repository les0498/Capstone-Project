# Generated by Django 4.1.7 on 2023-06-03 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_rename_phonenumber_user_phone_number"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
        migrations.DeleteModel(name="UserInfo",),
    ]
