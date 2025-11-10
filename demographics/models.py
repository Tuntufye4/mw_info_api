from django.db import models

class Demographics(models.Model):
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)   
    population = models.CharField(max_length=100)
    urban_percent = models.CharField(max_length=100)   
    name = models.CharField(max_length=100, blank=True, null=True)