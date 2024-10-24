# Generated by Django 4.2.15 on 2024-10-22 08:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("paymentApp", "0002_admission_invoice_table_paid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]