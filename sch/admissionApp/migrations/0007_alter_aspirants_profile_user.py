# Generated by Django 4.2.15 on 2024-10-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admissionApp", "0006_aspirants_profile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aspirants_profile",
            name="user",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
