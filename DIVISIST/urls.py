from django.contrib import admin
from django.urls import path, include
from gestion_academica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_academica.urls')),
]