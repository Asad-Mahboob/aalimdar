# Generated by Django 5.1.3 on 2024-12-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FIQH', 'Fiqh'), ('AQEEDAH', 'Aqeedah'), ('POETRY', 'Poetry'), ('HIKAYAT', 'Hikayat'), ('MASAIL', 'Masail')], max_length=50),
        ),
    ]
