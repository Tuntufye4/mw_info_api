from django.db import models

class Crop(models.Model):
    chichewa = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    scientific = models.CharField(max_length=100)

class Fish(models.Model):
    chichewa = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    scientific = models.CharField(max_length=100)

class Livestock(models.Model):
    chichewa = models.CharField(max_length=100)
    english = models.CharField(max_length=100)   
    scientific = models.CharField(max_length=100)
 