# Generated by Django 4.2.15 on 2024-11-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordApp", "0009_remove_cbt_execution_time_alter_cbt_execution_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cbt",
            name="duration",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
