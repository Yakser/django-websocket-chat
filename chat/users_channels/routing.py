from django.urls import re_path
from websockets.consumers import UsersChannelsConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_channel_name>\w+)/$',
            UsersChannelsConsumer.as_asgi()),
]
