from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

print(settings)
print('urls.py, settings.STATIC_URL:', settings.STATIC_URL)
print('urls.py, settings.STATIC_ROOT:', settings.STATIC_ROOT)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)