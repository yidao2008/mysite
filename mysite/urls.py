from django.contrib import admin
from django.urls import path,include
import xadmin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
import django.views
import settings.STATIC_ROOT



urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ueditor/', include(DjangoUeditor_urls)),
    path('static/', django.views.static.serve, {'document_root': STATIC_ROOT} ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
