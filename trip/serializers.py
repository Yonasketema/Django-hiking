from rest_framework import serializers
from .models import Trip, TripBooking


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'title', 'price']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripBooking
        fields = ['id', 'user',
                  'number_of_people', 'start_date', 'total_price']

    def create(self, validated_data):
        trip_id = self.context['trip_id']
        return TripBooking.objects.create(trip_id=trip_id, **validated_data)
