from django.urls import re_path
from websockets.consumers import GroupsConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<group_name>\w+)/$',
            GroupsConsumer.as_asgi()),
]
 