# Generated by Django 4.2.15 on 2024-10-07 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="cbt",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "course_title",
                    models.CharField(max_length=200, null=True, unique=True),
                ),
                (
                    "course_code",
                    models.CharField(max_length=30, null=True, unique=True),
                ),
                ("duration", models.TimeField(max_length=50, null=True)),
                ("execution_time", models.TimeField(max_length=50, null=True)),
                ("execution_date", models.DateField(max_length=50, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="course_model",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("no_of_courses", models.CharField(max_length=10)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="questions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=500, null=True)),
                ("first_option", models.CharField(max_length=500, null=True)),
                ("second_option", models.CharField(max_length=500, null=True)),
                ("third_option", models.CharField(max_length=500, null=True)),
                ("forth_option", models.CharField(max_length=500, null=True)),
                ("answer", models.CharField(max_length=500, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "cbt",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recordApp.cbt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="grading",
            fields=[
                ("excuted_time", models.DateTimeField(auto_created=True)),
                ("grade_id", models.AutoField(primary_key=True, serialize=False)),
                ("score", models.CharField(max_length=20, null=True)),
                (
                    "finished_time",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recordApp.cbt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="course_register",
            fields=[
                ("reg_id", models.AutoField(primary_key=True, serialize=False)),
                ("instructor", models.CharField(max_length=500)),
                ("course", models.CharField(max_length=100, unique=True)),
                (
                    "course_code",
                    models.CharField(max_length=30, null=True, unique=True),
                ),
                ("unit", models.CharField(max_length=10)),
                ("level", models.CharField(max_length=10, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("last_update", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "course_model",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recordApp.course_model",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cbt",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="recordApp.course_register",
            ),
        ),
        migrations.AddField(
            model_name="cbt",
            name="examiner",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
