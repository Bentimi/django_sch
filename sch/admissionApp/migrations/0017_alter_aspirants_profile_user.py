# Generated by Django 4.2.15 on 2024-11-04 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admissionApp", "0016_alter_admission_approval_aspirant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aspirants_profile",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
