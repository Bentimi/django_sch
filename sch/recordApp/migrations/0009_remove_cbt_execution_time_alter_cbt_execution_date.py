# Generated by Django 4.2.15 on 2024-11-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordApp", "0008_course_form_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cbt",
            name="execution_time",
        ),
        migrations.AlterField(
            model_name="cbt",
            name="execution_date",
            field=models.DateTimeField(max_length=50, null=True),
        ),
    ]
