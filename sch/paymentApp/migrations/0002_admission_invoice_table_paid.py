# Generated by Django 4.2.15 on 2024-10-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paymentApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission_invoice_table",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]
