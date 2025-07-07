from django.db import models

class CurrencyRate(models.Model):
    code = models.CharField(max_length=10, unique=True)
    rate_to_mwk = models.FloatField()
