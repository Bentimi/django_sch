# Generated by Django 4.2.15 on 2024-10-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordApp", "0007_remove_course_model_no_of_courses_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course_form",
            name="status",
            field=models.BooleanField(default=False),
        ),
    ]
