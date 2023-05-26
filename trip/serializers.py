from rest_framework import serializers
from .models import Trip, TripBooking


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'title', 'price',
                  'image_uri', 'description']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TripBooking
        fields = ['id',
                  'number_of_people', 'start_date', 'total_price']

    def create(self, validated_data):
        trip_id = self.context['trip_id']
        user_id = self.context['user_id']
        return TripBooking.objects.create(trip_id=trip_id, user=user_id, **validated_data)
