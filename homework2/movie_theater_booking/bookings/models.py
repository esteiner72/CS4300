from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    release_date = models.DateTimeField()
    duration = models.DecimalField(max_digits=5, decimal_places=2)

class Seat(models.Model):
    seat_num = models.IntegerField()
    status = models.BooleanField()

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
