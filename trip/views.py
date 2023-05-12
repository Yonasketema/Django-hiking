from rest_framework.viewsets import ModelViewSet

from .models import Trip, TripBooking
from .serializers import TripSerializer, BookingSerializer


class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripBookingViewSet(ModelViewSet):
    queryset = TripBooking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        return {'trip_id':  self.kwargs['trip_pk'], 'request': self.request}
