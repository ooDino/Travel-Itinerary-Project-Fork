from django.db import models


# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
