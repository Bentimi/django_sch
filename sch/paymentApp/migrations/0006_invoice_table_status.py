# Generated by Django 4.2.15 on 2024-10-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paymentApp", "0005_delete_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice_table",
            name="status",
            field=models.CharField(default="unsuccessful", max_length=50),
        ),
    ]
