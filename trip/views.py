from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Trip, TripBooking, HikingBooking, WeeklyHike
from .serializers import TripSerializer, TripBookingSerializer, WeeklyHikeSerializer, HikeBookingSerializer


class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class WeeklyHikeSet(ModelViewSet):
    queryset = WeeklyHike.objects.all()
    serializer_class = WeeklyHikeSerializer


class TripBookingViewSet(ModelViewSet):
    queryset = TripBooking.objects.all()
    serializer_class = TripBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'trip_id':  self.kwargs['trip_pk'], 'user_id': self.request.user, 'request': self.request}


class HikeBookingViewSet(ModelViewSet):
    queryset = HikingBooking.objects.all()
    serializer_class = HikeBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'hike_id':  self.kwargs['hike_pk'], 'user_id': self.request.user, 'request': self.request}


@api_view()
@permission_classes([IsAuthenticated])
def mytrip(resquest):
    mytrip = TripBooking.objects.filter(user=resquest.user)
    serializer = TripBookingSerializer(mytrip, many=True)
    return Response(serializer.data)
