from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Trip, TripBooking
from .serializers import TripSerializer, BookingSerializer


class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripBookingViewSet(ModelViewSet):
    queryset = TripBooking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'trip_id':  self.kwargs['trip_pk'], 'user_id': self.request.user, 'request': self.request}
