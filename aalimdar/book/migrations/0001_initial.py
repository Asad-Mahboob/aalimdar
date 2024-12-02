# Generated by Django 5.1.3 on 2024-12-01 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aalim_profile', '0002_remove_aalimprofile_books_alter_aalimprofile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('FIQH', 'Fiqh'), ('AQEEDAH', 'Aqeedah'), ('NAAT', 'Naat'), ('HIKAYAT', 'Hikayat'), ('MASAIL', 'Masail')], max_length=50)),
                ('language', models.CharField(choices=[('ENG', 'English'), ('UR', 'Urdu'), ('AR', 'Arabic'), ('PR', 'Persian')], max_length=50)),
                ('publication_date', models.CharField(blank=True, max_length=200, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='photos/book_covers/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/book_pdfs/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='aalim_profile.aalimprofile')),
            ],
        ),
    ]