from django.db import models

# Create your models here.
class videos(models.Model):
    Video = models.FileField(upload_to='uploaded')
    Sub = models.FileField(upload_to='uploaded')
