# Generated by Django 4.2.15 on 2024-11-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userApp", "0010_staff_table_staff_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="department",
            field=models.CharField(
                choices=[
                    ("Digital Marketing", "Digital Marketing"),
                    ("Business World", "Business World"),
                    ("Media Technology", "Media Technology"),
                    ("Communications", "Communications"),
                    ("Business Ethics", "Business Ethics"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
