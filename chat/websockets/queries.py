from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from users_messages.models import UserChatMessage, UserGroupMessage

from websockets.connection_types import CHATS_CONNECTION, GROUPS_CONNECTION
from websockets.errors import ConnectionTypeDoesNotExist
from websockets.helpers import (get_chat_daily_messages, get_chat_id,
                                get_group_daily_messages, get_group_slug)

User = get_user_model()


async def add_message_to_db(user: User, message_text: str, connection_name: str) -> None:
    """
    Добавляет сообщение в контейнер соответствующий типу подключения

    Args:
        user (User): отправитель
        message_text (str): текст сообщения
        connection_name (str): тип подключения

    Raises:
        ConnectionTypeDoesNotExist: несуществующий тип подключения
    """
    if connection_name.startswith(GROUPS_CONNECTION):
        await add_message_to_group(user, message_text, connection_name)
    elif connection_name.startswith(CHATS_CONNECTION):
        await add_message_to_chat(user, message_text, connection_name)
    else:
        raise ConnectionTypeDoesNotExist("Данный тип подключения не существует!")


@database_sync_to_async
def add_message_to_group(user: User, message_text: str, connection_name: str) -> None:
    """
    Создает сообщение в контейнере группы DailyGroupMessages

    Args:
        user (User): отправитель
        message_text (str): текст сообщения
        connection_name (str): имя подключения, для групп - GROUPS_CONNECTION_<group_name>
    """
    group_slug = get_group_slug(connection_name)
    group_daily_messages = get_group_daily_messages(group_slug)

    message = UserGroupMessage(user=user, text=message_text, container=group_daily_messages)
    message.save()


@database_sync_to_async
def add_message_to_chat(user: User, message_text: str, connection_name: str) -> None:
    """
    Создает сообщение в контейнере группы DailyChatMessages

    Args:
        user (User): отправитель
        message_text (str): текст сообщения
        connection_name (str): имя подключения, для чатов - CHATS_CONNECTION_<chat_id>
    """

    chat_id = get_chat_id(connection_name)
    chat_daily_messages = get_chat_daily_messages(chat_id)

    message = UserChatMessage(user=user, text=message_text, container=chat_daily_messages)
    message.save()
