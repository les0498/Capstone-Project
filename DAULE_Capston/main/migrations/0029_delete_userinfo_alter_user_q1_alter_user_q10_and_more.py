# Generated by Django 4.1.7 on 2023-06-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0028_alter_user_q1_alter_user_q10_alter_user_q2_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="UserInfo",),
        migrations.AlterField(
            model_name="user",
            name="q1",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="q10",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="q2",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="q3",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="q4",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="user",
            name="q5",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="user",
            name="q6",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="user",
            name="q7",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="user",
            name="q8",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="user",
            name="q9",
            field=models.CharField(default="", max_length=10),
        ),
    ]