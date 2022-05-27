import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from websockets.events import ChatMessageEventType
from websockets.queries import add_message_to_db
from websockets.types import (ChatMessageEvent, Message, WebsocketData,
                              WebsocketEvent)

User = get_user_model()


class BaseConsumer(AsyncWebsocketConsumer):
    """
    Асинхронный вебсокет consumer
    """
    async def connect(self):
        """
        Подключение к websocket группе
        """
        self.connection_name = self.scope['url_route']['kwargs']['group_name']
        self.connection_group_name = f'websocket_group_{self.connection_name}'

        # Вход в группу
        await self.channel_layer.group_add(
            self.connection_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code: int):
        """
        Осуществляет выход из группы

        Args:
            close_code (int): код выхода
        """

        await self.channel_layer.group_discard(
            self.connection_group_name,
            self.channel_name
        )

    async def receive(self, text_data: str):
        """
        Получает сообщения от вебсокета

        Args:
            text_data (str): строка с json объектом Message. Например '{"message": "message-text"}'
        """

        text_data_json: Message = json.loads(text_data)
        user: User = self.scope['user']

        message: str = text_data_json['message']
        username: str = user.username

        group_send_data: ChatMessageEvent = {
            'type': ChatMessageEventType.type,
            'message': message,
            'username': username
        }

        await self.channel_layer.group_send(
            self.connection_group_name,
            group_send_data
        )

        await add_message_to_db(user, message, self.connection_name)

    async def chat_message(self, event: WebsocketEvent):
        """
        Получает сообщения от websocket группы

        Args:
            event (WebsocketEvent): событие WebsocketEvent
        """

        message = event['message']
        username = event['username']

        data: WebsocketData = {
            'message': message,
            'username': username
        }

        await self.send(text_data=json.dumps(data))


class ChatsConsumer(BaseConsumer):
    pass


class GroupsConsumer(BaseConsumer):
    pass


class UsersChannelsConsumer(BaseConsumer):
    pass
