# Generated by Django 5.1.3 on 2024-11-11 20:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signageApp', '0004_alter_screen_screen_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='file_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
