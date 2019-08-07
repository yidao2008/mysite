from django.contrib import admin
from django.urls import path,include
import xadmin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ueditor/', include(DjangoUeditor_urls)),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
