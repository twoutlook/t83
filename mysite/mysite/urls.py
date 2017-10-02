from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^t83/', include('t83.urls')),
    url(r'^admin/', admin.site.urls),
]
