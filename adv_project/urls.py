from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
]
