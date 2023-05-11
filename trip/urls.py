from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('trips', views.TripViewSet)
router.register('booking', views.BooingViewSet)


urlpatterns = router.urls
