# Generated by Django 4.2.15 on 2024-10-02 14:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admissionApp", "0010_alter_aspirants_profile_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="aspirants_profile",
            old_name="create_time",
            new_name="created_time",
        ),
    ]