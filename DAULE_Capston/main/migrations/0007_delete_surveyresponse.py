# Generated by Django 4.1.7 on 2023-05-29 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_remove_response_question_remove_response_user_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="SurveyResponse",),
    ]
