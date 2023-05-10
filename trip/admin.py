from django.contrib import admin

from .models import Trip, Book


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_editable = ['price']
    list_per_page = 12


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['trip', 'booked_at', 'payment_status', ]
