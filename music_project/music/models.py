from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50,default='')
    release_date = models.DateTimeField()
    likes = models.IntegerField(default=0,null=False)