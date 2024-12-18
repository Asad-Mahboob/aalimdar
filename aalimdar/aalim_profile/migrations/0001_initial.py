# Generated by Django 5.1.3 on 2024-11-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AalimProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('dob', models.DateField()),
                ('dod', models.DateField(blank=True, null=True)),
                ('biography', models.TextField()),
                ('books', models.TextField(blank=True, null=True)),
                ('poetry', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
