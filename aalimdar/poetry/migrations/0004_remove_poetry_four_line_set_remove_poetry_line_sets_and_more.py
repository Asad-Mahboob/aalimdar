# Generated by Django 5.1.3 on 2024-12-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0003_remove_poetry_two_line_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poetry',
            name='four_line_set',
        ),
        migrations.RemoveField(
            model_name='poetry',
            name='line_sets',
        ),
        migrations.AddField(
            model_name='poetry',
            name='lines',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
