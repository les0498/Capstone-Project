# Generated by Django 4.1.7 on 2023-05-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_remove_question_question_text_question_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="response", name="question",),
        migrations.RemoveField(model_name="response", name="user",),
        migrations.DeleteModel(name="Choice",),
        migrations.DeleteModel(name="Question",),
        migrations.DeleteModel(name="Response",),
    ]