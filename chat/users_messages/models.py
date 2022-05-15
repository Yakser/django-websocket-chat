from chats.models import Chat
from core.models import BaseDailyMessages, BaseUserMessage
from django.contrib.auth import get_user_model
from django.db import models
from groups.models import Group
from users_channels.models import UsersChannel

User = get_user_model()


class DailyChatMessages(BaseDailyMessages):
    chat = models.ForeignKey(Chat,
                             on_delete=models.SET_NULL,
                             verbose_name='Чат',
                             related_name='chat_containers',
                             null=True
                             )

    class Meta:
        verbose_name = 'Контейнер сообщений чата'
        verbose_name_plural = 'Контейнеры сообщений чатов'


class DailyGroupMessages(BaseDailyMessages):
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              verbose_name='Группа',
                              related_name='group_containers',
                              null=True
                              )

    class Meta:
        verbose_name = 'Контейнер сообщений группы'
        verbose_name_plural = 'Контейнеры сообщений группы'


class DailyChannelMessages(BaseDailyMessages):
    channel = models.ForeignKey(UsersChannel,
                                on_delete=models.SET_NULL,
                                verbose_name='Канал',
                                related_name='channel_containers',
                                null=True
                                )

    class Meta:
        verbose_name = 'Контейнер сообщений канала'
        verbose_name_plural = 'Контейнеры сообщений канала'


class UserChatMessage(BaseUserMessage):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             verbose_name='Отправитель',
                             related_name='chat_messages',
                             null=True
                             )
    container = models.ForeignKey(DailyChatMessages,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Контейнер',
                                  related_name='chat_messages',
                                  null=True
                                  )

    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чата'


class UserGroupMessage(BaseUserMessage):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             verbose_name='Отправитель',
                             related_name='group_messages',
                             null=True
                             )
    container = models.ForeignKey(DailyGroupMessages,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Контейнер',
                                  related_name='group_messages',
                                  null=True
                                  )

    class Meta:
        verbose_name = 'Сообщение группы'
        verbose_name_plural = 'Сообщения группы'


class UserChannelMessage(BaseUserMessage):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             verbose_name='Отправитель',
                             related_name='channel_messages',
                             null=True
                             )
    container = models.ForeignKey(DailyChannelMessages,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Контейнер',
                                  related_name='channel_messages',
                                  null=True
                                  )

    class Meta:
        verbose_name = 'Сообщение канала'
        verbose_name_plural = 'Сообщения канала'
