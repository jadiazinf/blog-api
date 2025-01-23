import pytest
from django.core.exceptions import ValidationError
from locations.models import Location
from tests.locations.location_factory import LocationFactory

@pytest.mark.django_db
class TestLocationModel:

    def test_create_country(self):
        country = LocationFactory.country()
        assert Location.objects.filter(id=country.id).exists()

    def test_create_state(self):
        state = LocationFactory.state()
        assert Location.objects.filter(id=state.id).exists()

    def test_create_city(self):
        city = LocationFactory.city()
        assert Location.objects.filter(id=city.id).exists()

    def test_create_with_invalid_type(self):
        with pytest.raises(ValidationError):
            location = LocationFactory.with_invalid_type()
            location.full_clean()

    def test_create_with_invalid_parent(self):
        with pytest.raises(ValidationError):
            location = LocationFactory.with_invalid_parent()
            location.full_clean()

