# Generated by Django 4.2.6 on 2023-10-16 15:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quizApp", "0006_quiz_quiz"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quiz",
            name="quiz",
        ),
    ]
