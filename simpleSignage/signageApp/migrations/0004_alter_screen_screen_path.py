# Generated by Django 5.1.3 on 2024-11-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signageApp', '0003_screen_screen_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='screen_path',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
