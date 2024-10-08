# Generated by Django 4.2.15 on 2024-09-28 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="department",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="level",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="matric_no",
        ),
        migrations.AddField(
            model_name="profile",
            name="category",
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.CreateModel(
            name="users_status",
            fields=[
                ("status_id", models.AutoField(primary_key=True, serialize=False)),
                ("student", models.BooleanField(default=False)),
                ("staff", models.BooleanField(default=False)),
                ("aspirant", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userApp.profile",
                    ),
                ),
            ],
        ),
    ]
