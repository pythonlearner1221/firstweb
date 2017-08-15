from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    episodes = models.IntegerField(blank=True)
    length = models.IntegerField(blank=True)
    name = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    seasons = models.IntegerField(blank=True)
    status = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    url = models.CharField(max_length=100)
    users = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
