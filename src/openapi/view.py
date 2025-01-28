from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from decouple import config

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version=config('API_VERSION', default='v1'),
      description="This is the API documentation for the Blog API backend project",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jadiaz.inf@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
