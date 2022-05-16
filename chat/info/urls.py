from django.urls import path

from info.views import AboutView, InstructionView

app_name = 'info'
urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('instruction', InstructionView.as_view(), name='instruction'),
]
