from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('mainapp.urls')),
    url(r'^', include('mainapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
