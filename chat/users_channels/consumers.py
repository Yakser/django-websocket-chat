import json

from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser


class UsersChannelsConsumer(WebsocketConsumer):
    def connect(self):
        self.user_channel_name = self.scope['url_route']['kwargs']['game_id']
        self.user_channel_group_name = f'Channel {self.channel_name}'

        if self.scope['user'] == AnonymousUser():
            raise DenyConnection("Такого пользователя не существует")

        async_to_sync(self.channel_layer.group_add)(
            self.user_channel_group_name,
            self.channel_name
        )

        self.accept()
        

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.user_channel_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to  group
        async_to_sync(self.channel_layer.group_send)(
            self.user_channel_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        
    # Receive message from group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))