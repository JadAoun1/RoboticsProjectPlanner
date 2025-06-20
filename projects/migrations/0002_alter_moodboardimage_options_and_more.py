# Generated by Django 5.2.3 on 2025-06-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="moodboardimage",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="projectpart",
            options={"ordering": ["part_name"]},
        ),
        migrations.AlterModelOptions(
            name="projecttool",
            options={"ordering": ["tool_name"]},
        ),
        migrations.RemoveField(
            model_name="projectpart",
            name="cost_per_unit",
        ),
        migrations.AddField(
            model_name="projectpart",
            name="actual_cost_per_unit",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="projectpart",
            name="estimated_cost_per_unit",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="moodboardimage",
            name="caption",
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name="projectnote",
            name="title",
            field=models.CharField(blank=True, default="Note", max_length=200),
        ),
    ]
