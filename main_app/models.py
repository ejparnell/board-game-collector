from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    player_count = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
