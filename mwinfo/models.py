from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    capital = models.CharField(max_length=100, null=True)
    population_2023 = models.IntegerField()
    area_km2 = models.FloatField()
    density = models.FloatField()
    elevation_m = models.IntegerField()
    climate = models.CharField(max_length=100) 
    timezone = models.CharField(max_length=50)
    languages = models.CharField(max_length=50, null=True)   
            