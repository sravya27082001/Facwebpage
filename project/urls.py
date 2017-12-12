
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from project import views

urlpatterns = [
    url(r'^$',views.login_redirect,name='login_redirect'),
    url(r'^fac/', include('fac.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

