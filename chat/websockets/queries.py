from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from users_messages.models import UserGroupMessage

from websockets.helpers import get_group_daily_messages, get_group_slug

User = get_user_model()


@database_sync_to_async
def add_message_to_group(user: User, message_text: str, connection_name: str) -> None:
    """
    Добавляет сообщение в контейнер группы DailyGroupMessages

    Args:
        user (User): отправитель
        message_text (str): текст сообщения
        connection_name (str): имя подключения, для групп - GROUPS_CONNECTION_<group_name>
    """
    group_slug = get_group_slug(connection_name)
    group_daily_messages = get_group_daily_messages(group_slug)

    message = UserGroupMessage(user=user, text=message_text, container=group_daily_messages)
    message.save()
