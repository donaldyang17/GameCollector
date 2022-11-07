from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField()
        
    def __str__(self):
        return self.name