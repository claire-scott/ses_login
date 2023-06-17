from django.conf.urls import url, include 
from rest_framework.routers import DefaultRouter
from apps.checkin.views import UnitViewSet, EventViewSet

router = DefaultRouter()
router.register("units", UnitViewSet, basename="units")
router.register("events", UnitViewSet, basename="events")
notes_urlpatterns = [url("api/v1/", include(router.urls))]