from django.db import models
from django.urls import reverse

RATINGS = (
    ('E', 'Excellent'),
    ('G', 'Good'),
    ('F', 'Fair'),
    ('P','Poor'),
)

class Character(models.Model):
    name = models.CharField(max_length=100) 
    gender = models.CharField(max_length=100)
    description = models.TextField(max_length=250) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('characters_detail', kwargs={'pk': self.id})


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField()
    characters = models.ManyToManyField(Character)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Rating(models.Model):
    date = models.DateField('Date Rating Was Created:')
    rate = models.CharField(max_length=1, choices = RATINGS, default = [0][0])
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_rate_display()} on {self.date}"
    class Meta:
        ordering = ['-date']