import factory
from locations.models import Location
import uuid

class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location
        skip_postgeneration_save = True

    id = factory.LazyFunction(uuid.uuid4)
    name = factory.Faker("city")
    type = factory.Iterator(Location.LocationType.values)
    parent = None

    @classmethod
    def attrs(cls, **kwargs):
        return factory.build(dict, FACTORY_CLASS=cls, **kwargs)

    @factory.post_generation
    def with_parent(obj, create, extracted, **kwargs):
        if extracted:
            obj.parent = extracted
            if create:
                obj.save()

    @classmethod
    def country(cls, **kwargs):
        return cls(type=Location.LocationType.COUNTRY, **kwargs)

    @classmethod
    def state(cls, parent=None, **kwargs):
        if not parent:
            parent = cls.country()
        return cls(type=Location.LocationType.STATE, parent=parent, **kwargs)

    @classmethod
    def city(cls, parent=None, **kwargs):
        if not parent:
            parent = cls.state()
        return cls(type=Location.LocationType.CITY, parent=parent, **kwargs)

    @classmethod
    def with_invalid_type(cls, **kwargs):
        location = cls(type="INVALID_TYPE", **kwargs)
        location.save()
        return location

    @classmethod
    def with_invalid_parent(cls, **kwargs):
        location = cls(type=Location.LocationType.CITY, parent=cls.country(), **kwargs)
        location.save()
