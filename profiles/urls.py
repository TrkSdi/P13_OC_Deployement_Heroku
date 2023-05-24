from django.urls import path

from . import views


app_name = 'profiles'
urlpatterns = [
    path('', views.index, name='profile_index'),
    path('<str:username>/', views.profile, name='profiles_id'),
]
