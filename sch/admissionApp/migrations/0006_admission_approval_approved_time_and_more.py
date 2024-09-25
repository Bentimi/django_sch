# Generated by Django 4.2.15 on 2024-09-25 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admissionApp", "0005_aspirants_profile_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission_approval",
            name="approved_time",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="admission_approval",
            name="officer_incharge",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="aspirants_profile",
            name="course",
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
        migrations.AddField(
            model_name="aspirants_profile",
            name="create_time",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="aspirants_profile",
            name="last_login",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="aspirants_profile",
            name="national_identity",
            field=models.FileField(
                null=True, unique=True, upload_to="naional_identityImage/"
            ),
        ),
        migrations.AddField(
            model_name="aspirants_profile",
            name="next_of_kin_address",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="aspirants_profile",
            name="next_of_kin",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="aspirants_profile",
            name="phone_no",
            field=models.CharField(max_length=25, unique=True),
        ),
    ]