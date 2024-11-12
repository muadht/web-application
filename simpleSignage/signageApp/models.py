from django.db import models
import re

# Create your models here.
# I need to store user assests: images, videos, and text
# file type, file name, file path, file size, file upload date, user id

class Asset(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_type = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    file_size = models.CharField(max_length=100, blank=True)
    file_upload_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(null=True, blank=True)
    file_url = models.URLField(max_length=200)

    def __str__(self):
        return self.file_name

class Screen(models.Model):
    screen_id = models.AutoField(primary_key=True)
    screen_name = models.CharField(max_length=100)
    screen_path = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        sanitized_name = re.sub(r'[^a-z0-9]+', '-', self.screen_name.lower().replace(' ', '-')).strip('-')
        sanitized_location = re.sub(r'[^a-z0-9]+', '-', self.screen_location.lower().replace(' ', '-')).strip('-')
        self.screen_path = f"{sanitized_name}-{sanitized_location}"
        super(Screen, self).save(*args, **kwargs)
    screen_resolution = models.CharField(max_length=100)
    screen_location = models.CharField(max_length=100)
    screen_orientation = models.CharField(max_length=100)
    screen_status = models.CharField(max_length=100)
    screen_last_updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.screen_name