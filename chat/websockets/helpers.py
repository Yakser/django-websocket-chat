from django.shortcuts import get_object_or_404
from websockets.connection_types import GROUPS_CONNECTION
from groups.models import Group
from users_messages.models import DailyGroupMessages


def get_group_slug(connection_name: str) -> str:
    """
    Убирает GROUPS_CONNECTION из имени подключения и возвращает slug группы.
    Если имя подключения не соответствует подключению группы, то возвращается None
    Args:
        connection_name (str): имя подключения, для групп - groups_<group_name>

    Returns:
        str: slug группы
        None: если имя подключение не соответствует группе
    """
    if connection_name.startswith(GROUPS_CONNECTION):
        return connection_name[len(GROUPS_CONNECTION) + 1:]


def get_group_daily_messages(group_slug: str) -> DailyGroupMessages:
    try:
        group = get_object_or_404(Group, pk=group_slug)

        return DailyGroupMessages.objects.get(group=group)

    except DailyGroupMessages.DoesNotExist:
        print(f"Контейнера DailyGroupMessages для группы {group_slug} не существует!")
