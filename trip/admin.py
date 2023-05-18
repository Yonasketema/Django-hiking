from django.contrib import admin

from .models import Trip, TripBooking, GuideProfile, Location, Category, WeeklyHike, HikingBooking


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_editable = ['price']
    list_per_page = 12


@admin.register(WeeklyHike)
class WeeklyHikeAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'start_date',  'price', 'guide',]
    list_editable = ['price']
    list_per_page = 12


@admin.register(TripBooking)
class TripBookingAdmin(admin.ModelAdmin):
    list_display = ['trip',  'payment_status', ]


@admin.register(HikingBooking)
class HikingBookingAdmin(admin.ModelAdmin):
    list_display = ['weekly_hike',  'payment_status', ]


@admin.register(GuideProfile)
class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image_uri']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
