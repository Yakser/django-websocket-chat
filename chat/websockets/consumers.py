import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class BaseConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.group_group_name = 'chat_%s' % self.group_name

        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.group_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Send message to  group
        async_to_sync(self.channel_layer.group_send)(
            self.group_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from group
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))


class GroupsConsumer(BaseConsumer):
    pass


class UsersChannelsConsumer(BaseConsumer):
    pass
