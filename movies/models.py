from django.db import models

# Create your models here.
class Moviedata(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    ratings = models.FloatField()