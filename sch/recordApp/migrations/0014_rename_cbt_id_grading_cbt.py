# Generated by Django 4.2.15 on 2024-11-07 22:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recordApp", "0013_grading_active"),
    ]

    operations = [
        migrations.RenameField(
            model_name="grading",
            old_name="cbt_id",
            new_name="cbt",
        ),
    ]
