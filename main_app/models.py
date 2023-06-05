from django.db import models
from django.urls import reverse


# Create your models here.
STATUSES = (("W", "Won"), ("L", "Lost"))
STORES = (("F", "Friendly Local Game Store"), ("O", "Online"), ("B", "Big Box Store"))


class Store(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=STORES, default=STORES[0][0])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stores_detail", kwargs={"pk": self.id})


class Game(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    player_count = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"game_id": self.id})

    def win_count(self):
        wins = self.play_set.filter(status="W").count()
        return wins

    def loss_count(self):
        losses = self.play_set.filter(status="L").count()
        return losses


class Play(models.Model):
    date = models.DateField("play date")
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUSES[0][0])
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
