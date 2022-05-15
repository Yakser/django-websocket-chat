import json

from channels.generic.websocket import AsyncWebsocketConsumer

from websockets.queries import add_message


class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.connection_name = self.scope['url_route']['kwargs']['group_name']
        self.connection_group_name = f"websocket_group_{self.connection_name}"

        # Join group
        await self.channel_layer.group_add(
            self.connection_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.connection_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = self.scope['user']

        message = text_data_json['message']
        username = user.username

        # Send message to group
        await self.channel_layer.group_send(
            self.connection_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

        await add_message(user, message, self.connection_name)

    # Receive message from room group

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))


class ChatsConsumer(BaseConsumer):
    pass


class GroupsConsumer(BaseConsumer):
    pass


class UsersChannelsConsumer(BaseConsumer):
    pass
