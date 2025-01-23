from django.db import models
from .helpers import LocationHelpers
import uuid

class Location(models.Model):
    class LocationType(models.TextChoices):
        COUNTRY = 'COUNTRY', 'Country'
        STATE = 'STATE', 'State'
        CITY = 'CITY', 'City'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=50, choices=LocationType.choices, null=False, blank=False)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        db_table = 'locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

    def clean(self):
        helpers = LocationHelpers(self)
        helpers.validate_location_parent()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
