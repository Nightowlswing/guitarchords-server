from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length = 255)
    text = models.TextField()
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length = 255)
    compositor = models.ForeignKey('api.Compositor', related_name='songs', on_delete=models.CASCADE)
    genre = models.CharField(max_length = 255)
    capo = models.CharField(max_length = 255)
    text = models.TextField()
    def __str__(self):
        return self.name

class Compositor(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name