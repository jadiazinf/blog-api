from rest_framework.viewsets import ViewSet
from rest_framework import status
from locations.serializer import LocationSerializer
from rest_framework.response import Response
from locations.services import LocationServices
from rest_framework.permissions import AllowAny, IsAuthenticated

class LocationController(ViewSet):
    public_actions = ['list', 'retrieve']

    def get_permissions(self):
        if self.action in self.public_actions:
            return [AllowAny()]
        return [IsAuthenticated()]

    def list(self, _):
        locations = LocationServices.get_all_locations()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, _, pk=None):
        location = LocationServices.get_location_by_id(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            location = LocationServices.create_location(serializer.validated_data)
            return Response(LocationSerializer(location).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            location = LocationServices.update_location(pk, serializer.validated_data)
            return Response(LocationSerializer(location).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, _, pk=None):
        LocationServices.delete_location(pk)
        return Response({"message": "Location deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
