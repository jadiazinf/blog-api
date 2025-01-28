from .models import Location
from django.shortcuts import get_object_or_404

class LocationServices():
    @staticmethod
    def get_all_locations():
        return Location.objects.all()

    @staticmethod
    def get_location_by_id(location_id):
        return get_object_or_404(Location, id=location_id)

    @staticmethod
    def create_location(data):
        location = Location.objects.create(**data)
        return location

    @staticmethod
    def update_location(location_id, data):
        location = get_object_or_404(Location, id=location_id)
        for key, value in data.items():
            setattr(location, key, value)
        location.save()
        return location

    @staticmethod
    def delete_location(location_id):
        location = get_object_or_404(Location, id=location_id)
        location.delete()
