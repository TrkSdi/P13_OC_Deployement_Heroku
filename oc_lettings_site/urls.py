from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),  
]
