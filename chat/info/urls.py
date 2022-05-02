from django.urls import path

from info.views import AboutView, InstroctionView

app_name = 'info'
urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('instruction', InstroctionView.as_view(), name='instruction'),
]
