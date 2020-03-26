from django.db import models

# Create your models here.
class videos(models.Model):
    Video = models.FileField(upload_to='uploaded')
    Sub = models.FileField(upload_to='uploaded')

class chunk(models.Model):
    chunk=models.IntegerField()
    Time_start=models.CharField(max_length=30)
    Time_end=models.CharField(max_length=30)
    Sequence = models.IntegerField()
    Subtitle = models.TextField()
    Audio = models.FileField(upload_to='Audio/')
    Video = models.FileField(upload_to='Video/')

class uploaded_audio(models.Model):
    Audio = models.FileField(upload_to='uploaded')