from django.core.exceptions import ValidationError

class LocationHelpers():
    def __init__(self, location):
        self.location = location

    def validate_location_parent(self):
        if self.location.type == self.location.LocationType.CITY:
            if not self.location.parent:
                raise ValidationError("A city must have a parent.")
            if self.location.parent.type != self.location.LocationType.STATE:
                raise ValidationError(f"The parent of {self.location.name} (type: {self.location.type}) must be a state.")
        elif self.location.type == self.location.LocationType.STATE:
            if not self.location.parent:
                raise ValidationError("A state must have a parent.")
            if self.location.parent.type != self.location.LocationType.COUNTRY:
                raise ValidationError(f"The parent of {self.location.name} (type: {self.location.type}) must be a country.")
        elif self.location.type == self.location.LocationType.COUNTRY:
            if self.location.parent:
                raise ValidationError("A country cannot have a parent.")
