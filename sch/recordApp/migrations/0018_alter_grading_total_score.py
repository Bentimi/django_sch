# Generated by Django 4.2.15 on 2024-11-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordApp", "0017_grading_total_score_grading_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grading",
            name="total_score",
            field=models.IntegerField(null=True),
        ),
    ]