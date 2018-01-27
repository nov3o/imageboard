from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from board.admin import admin_site

urlpatterns = patterns('',
    (r'^', include('board.urls')),
    (r'^admin/', include(admin_site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)