from django.db import models

class Pin(models.Model):
    type = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cross_street = models.CharField(max_length=200)
    rating = models.IntegerField()
