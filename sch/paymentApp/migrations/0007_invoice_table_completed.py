# Generated by Django 4.2.15 on 2024-10-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paymentApp", "0006_invoice_table_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice_table",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
