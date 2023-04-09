from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = \
    [
        path('api/v1/', include('kitchen.api.urls')),
        path('grappelli/', include('grappelli.urls')),
        path('admin/', admin.site.urls),
        path('__debug__/', include('debug_toolbar.urls')),
        path('', include('kitchen.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
