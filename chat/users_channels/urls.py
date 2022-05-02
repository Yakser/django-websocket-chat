from django.urls import path

from users_channels.views import UsersChannelsView

app_name = 'users_channels'
urlpatterns = [
    path('<slug:channel_name>/', UsersChannelsView.as_view(), name='users_channels'),
]
