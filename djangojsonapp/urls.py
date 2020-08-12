from django.contrib import admin
from django.urls import path, include
from djsonapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djsonapi.urls'))
]
