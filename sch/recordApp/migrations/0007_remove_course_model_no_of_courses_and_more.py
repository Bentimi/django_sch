# Generated by Django 4.2.15 on 2024-10-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordApp", "0006_course_form_units"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course_model",
            name="no_of_courses",
        ),
        migrations.AddField(
            model_name="course_model",
            name="course",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]