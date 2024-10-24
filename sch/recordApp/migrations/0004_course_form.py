# Generated by Django 4.2.15 on 2024-10-09 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recordApp", "0003_alter_cbt_examiner_alter_questions_cbt"),
    ]

    operations = [
        migrations.CreateModel(
            name="course_form",
            fields=[
                ("course_form_id", models.AutoField(primary_key=True, serialize=False)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "cbt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recordApp.cbt",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recordApp.course_register",
                    ),
                ),
                (
                    "score",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recordApp.grading",
                    ),
                ),
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
    ]