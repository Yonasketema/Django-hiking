from rest_framework import serializers
from .models import Trip, TripBooking, WeeklyHike, HikingBooking


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'title', 'price',
                  'image_uri', 'description']


class WeeklyHikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyHike
        fields = ['id', 'title', 'price', 'start_date', 'end_date',
                  'image_uri', 'description',]


class TripBookingSerializer(serializers.ModelSerializer):
    trip = TripSerializer(read_only=True)

    class Meta:
        model = TripBooking
        fields = ['id',
                  'number_of_people', 'start_date', 'total_price', 'trip']

    def create(self, validated_data):
        trip_id = self.context['trip_id']
        user_id = self.context['user_id']
        return TripBooking.objects.create(trip_id=trip_id, user=user_id, **validated_data)


class HikeBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = HikingBooking
        fields = ['id',
                  'number_of_people',  'total_price']

    def create(self, validated_data):
        hike_id = self.context['hike_id']
        user_id = self.context['user_id']
        return HikingBooking.objects.create(weekly_hike_id=hike_id, user=user_id, **validated_data)
