from django.urls import path
from rest_framework.routers import DefaultRouter
from locations.controller import LocationController

router = DefaultRouter()
router.register(r'locations', LocationController, basename='locations')

urlpatterns = router.urls
