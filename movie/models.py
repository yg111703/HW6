from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    percent = models.FloatField(max_length=50)
    body = models.TextField()