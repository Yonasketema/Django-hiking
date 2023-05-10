from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Trip, Book
from .serializers import TripSerializer, BookSerializer


@api_view()
def get_trip(request):

    # query = Book.objects.all()
    query = Trip.objects.all()

    serializer = TripSerializer(query, many=True)

    return Response(serializer.data)
