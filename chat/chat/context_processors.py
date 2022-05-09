from groups.models import Group
from users_messages.models import DailyGroupMessages
from django.db.models import Prefetch


def get_groups():
    groups = Group.objects.all()
    return groups


def chats(request):
    groups = get_groups()
    return {"chats_list": groups}