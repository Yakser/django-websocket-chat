from groups.models import Group
from users_messages.models import DailyGroupMessages
from django.db.models import Prefetch


def get_groups():
    groups = Group.objects.all()
    # TODO добавить список каналов и чатов с пользователями
    return groups


def chats(request):
    groups = get_groups()
    return {"chats_list": groups}
