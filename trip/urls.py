from . import views
from django.urls import path
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('trips', views.TripViewSet)
router.register('hikings', views.WeeklyHikeSet)


trip_router = routers.NestedDefaultRouter(router, 'trips', lookup='trip')
trip_router.register('booking', views.TripBookingViewSet,
                     basename='trip-booking')

hike_router = routers.NestedDefaultRouter(router, 'hikings', lookup='hike')
hike_router.register('booking', views.HikeBookingViewSet,
                     basename='hike-booking')


urlpatterns = [
    path('mytrip', views.mytrip)
] + router.urls + trip_router.urls + hike_router.urls
