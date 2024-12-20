# Generated by Django 4.2.15 on 2024-11-01 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("admissionApp", "0016_alter_admission_approval_aspirant"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("paymentApp", "0011_alter_admission_invoice_table_date_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admission_invoice_table",
            name="aspirant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="admissionApp.aspirants_profile",
            ),
        ),
        migrations.AlterField(
            model_name="latereg_invoice_table",
            name="tuition",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="paymentApp.tuition_invoice_table",
            ),
        ),
        migrations.AlterField(
            model_name="latereg_invoice_table",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="tuition_invoice_table",
            name="invoice",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="paymentApp.invoice_table",
            ),
        ),
        migrations.AlterField(
            model_name="tuition_invoice_table",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
