# Generated by Django 5.1.3 on 2024-12-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0004_remove_poetry_four_line_set_remove_poetry_line_sets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poetry',
            name='lines',
            field=models.TextField(),
        ),
    ]
