from django.urls import path

from homepage.views import HomeView

app_name = 'homepage'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
