from django.contrib import admin
from django.urls import include, path

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path('sentry-debug/', trigger_error),
]
