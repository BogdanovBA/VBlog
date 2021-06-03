from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from InfoBlog.views import *
from vblog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('InfoBlog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
handler403 = access_denied
