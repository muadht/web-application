# Generated by Django 5.1.3 on 2024-11-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signageApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('screen_id', models.AutoField(primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=100)),
                ('screen_resolution', models.CharField(max_length=100)),
                ('screen_location', models.CharField(max_length=100)),
                ('screen_orientation', models.CharField(max_length=100)),
                ('screen_status', models.CharField(max_length=100)),
                ('screen_last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
