from django.db import models

# Create your models here.
# travel_itinerary_app/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add user-related fields like profile picture, etc.

class TravelPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    # Add other fields as needed

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # Duration in days
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.destination


class ItineraryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.activity