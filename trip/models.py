from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GuideProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    image_uri = models.CharField(max_length=255)


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(Category)


class Trip(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    guide = models.ForeignKey(GuideProfile, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image_uri = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class WeeklyHike(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    day_of_week = models.PositiveIntegerField()
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    max_people = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    guide = models.ForeignKey(GuideProfile, on_delete=models.CASCADE)
    image_uri = models.CharField(max_length=255)


class Booking(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    trip = models.ForeignKey(
        Trip, on_delete=models.CASCADE, null=True, blank=True)
    weekly_hike = models.ForeignKey(
        WeeklyHike, on_delete=models.CASCADE, null=True, blank=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    booking_date = models.DateField(auto_now_add=True)
    number_of_people = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (("user", "trip"), ("user", "weekly_hike"))

    def __str__(self) -> str:

        return f'{self.user.username}'
