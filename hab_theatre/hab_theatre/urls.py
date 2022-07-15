from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

theatre = ''

urlpatterns = [
    path('admin/', admin.site.urls),
    path(theatre, include('theatre.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
