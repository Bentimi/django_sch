# Generated by Django 4.2.15 on 2024-10-16 08:11

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
            name="fees_table",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Full_tuition_fee", models.CharField(max_length=250, null=True)),
                ("part_tuition_fee", models.CharField(max_length=250, null=True)),
                ("late_reg_fee", models.CharField(max_length=250, null=True)),
                ("late_reg_approval", models.BooleanField(default=False)),
                ("admission_form_fee", models.CharField(max_length=250, null=True)),
                ("last_updated", models.CharField(max_length=250, null=True)),
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
    ]
