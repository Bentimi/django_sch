# Generated by Django 4.2.15 on 2024-11-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userApp", "0006_alter_profile_next_of_kin_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student_table",
            name="sequence",
            field=models.PositiveIntegerField(default=1, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name="student_table",
            name="status",
            field=models.CharField(default="Active", max_length=15),
        ),
        migrations.AlterField(
            model_name="student_table",
            name="date_added",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="student_table",
            name="department",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="student_table",
            name="year",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
