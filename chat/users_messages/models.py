from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseUserMessage, BaseDailyMessagesContainer

from groups.models import Group

from users_channels import UsersChannel

User = get_user_model()


class DailyMessagesGroupsContainer(BaseDailyMessagesContainer):
    group = models.ForeignKey(Group,
                                on_delete=models.SET_NULL,
                                verbose_name='Группа',
                                related_name='containers'
                                )


class DailyMessagesChannelsContainer(BaseDailyMessagesContainer):
    channel = models.ForeignKey(UsersChannel,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Канал',
                                    related_name='containers')


class UserGroupMessage(BaseUserMessage):
    container = models.ForeignKey(DailyMessagesGroupsContainer,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Контейнер',
                                    related_name='messages')


class UserChannelMessage(BaseUserMessage):
    container = models.ForeignKey(DailyMessagesChannelsContainer,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Контейнер',
                                    related_name='messages')
