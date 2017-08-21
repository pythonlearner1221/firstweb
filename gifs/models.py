from django.db import models
from datetime import datetime

# Create your models here.
class GifPics(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    created_time = models.DateTimeField()
    gif_index = models.IntegerField(primary_key=True)
    likes = models.IntegerField(blank=True,default=0)
    types = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title

    def get_date(self):
        year = self.created_time.year
        month = self.created_time.month
        day = self.created_time.day
        date = '{}年{}月{}日'.format(year,month,day)
        return date