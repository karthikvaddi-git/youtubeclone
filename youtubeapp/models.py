from django.db import models
from .backend import MediaStorage

# Create your models here.
class Video(models.Model):
    video1thumbnail = models.ImageField(storage=MediaStorage())
    video_title = models.CharField(max_length=255)
    video_desc = models.TextField()
    video = models.FileField(storage=MediaStorage())

    def __str__(self):
        return self.video_title






