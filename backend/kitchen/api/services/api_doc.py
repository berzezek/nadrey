from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="nadrey API",
        default_version='v1',
        description="Test description",
        terms_of_service="http://localhost/api/v1/",
        contact=openapi.Contact(email="wknduz@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)