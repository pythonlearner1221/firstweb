from django.db import models

# Create your models here.
class GifPics(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    created_time = models.CharField(max_length=100)
    gif_index = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title
