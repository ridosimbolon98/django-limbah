from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('autentikasi/', include('autentikasi.urls')),
    path('limbah/', include('limbah.urls')),
    path('users/', include('users.urls')),
    path('so/', include('so.urls')),
    path('admin/', admin.site.urls),
]

