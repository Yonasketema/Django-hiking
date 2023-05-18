from . import views
from django.urls import path
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('trips', views.TripViewSet)
# router.register('booking', views.TripBookingViewSet)

trip_router = routers.NestedDefaultRouter(router, 'trips', lookup='trip')
trip_router.register('booking', views.TripBookingViewSet,
                     basename='trip-booking')


urlpatterns = [
    path('mytrip', views.mytrip)
] + router.urls + trip_router.urls
