# Generated by Django 5.0.1 on 2024-01-08 15:09

import django.db.models.deletion
import users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('address_1', models.CharField(blank=True, max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]
