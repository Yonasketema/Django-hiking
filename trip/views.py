from rest_framework.viewsets import ModelViewSet

from .models import Trip, Booking
from .serializers import TripSerializer, BookingSerializer


class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class BooingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
