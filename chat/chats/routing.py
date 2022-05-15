from django.urls import re_path
from websockets.consumers import ChatsConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_id>\w+)/$',
            ChatsConsumer.as_asgi()),
]
