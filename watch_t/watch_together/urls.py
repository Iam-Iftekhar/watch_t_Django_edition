from django.urls import path
from . import views
from django.urls import path, include, re_path

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('watch/<str:room_name>/', views.watch_room, name='watch_room'),
    # Add more paths as you create more views
]