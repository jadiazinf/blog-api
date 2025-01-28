import pytest
from rest_framework.test import APIClient
from rest_framework import status
from tests.locations.factory import LocationFactory
from locations.models import Location

@pytest.mark.django_db
class TestLocationController:
    def setup_method(self):
        self.client = APIClient()

    def test_list_locations(self):
        response = self.client.get('/api/v1/locations/')
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_location(self):
        location = LocationFactory.build()
        response = self.client.get(f'/api/v1/locations/{location.id}/')
        assert response.status_code == status.HTTP_200_OK

    def test_create_location(self): # needs authentication
        payload = LocationFactory.attrs(type=Location.LocationType.COUNTRY)

        if payload['parent'] is None:
            del payload['parent']

        response = self.client.post('/api/v1/locations/', payload)
        assert response.status_code == status.HTTP_201_CREATED

    # def test_update_location(self):
    #     # Crea un objeto de prueba
    #     from locations.models import Location
    #     location = Location.objects.create(name="Old Location", description="Old Description")

    #     # Realiza una solicitud PUT al endpoint `update`
    #     payload = {"name": "Updated Location", "description": "Updated Description"}
    #     response = self.client.put(f'/api/v1/locations/{location.id}/', payload)

    #     # Verifica el código de respuesta
    #     assert response.status_code == status.HTTP_200_OK

    # def test_delete_location(self):
    #     # Crea un objeto de prueba
    #     from locations.models import Location
    #     location = Location.objects.create(name="To Delete", description="To Delete")

    #     # Realiza una solicitud DELETE al endpoint `destroy`
    #     response = self.client.delete(f'/api/v1/locations/{location.id}/')

    #     # Verifica el código de respuesta
    #     assert response.status_code == status.HTTP_204_NO_CONTENT
