from django.urls import path

from homepage.views import HomeView, room

app_name = 'homepage'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('room/<str:room_name>/', room, name='room'),
]
