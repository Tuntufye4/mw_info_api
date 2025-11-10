from django.db import models

class Healthdata(models.Model):
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    health_centers = models.CharField(max_length=100)
    hospitals = models.CharField(max_length=100)     
    dispensaries = models.CharField(max_length=100)
    

    