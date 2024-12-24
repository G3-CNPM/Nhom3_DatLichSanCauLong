from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    booking_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Revenue(models.Model):
    date = models.DateField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
