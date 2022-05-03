from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseUserMessage, BaseDailyMessages

from groups.models import Group

from users_channels.models import UsersChannel

User = get_user_model()


class DailyMessagesGroup(BaseDailyMessages):
    group = models.ForeignKey(Group,
                                on_delete=models.SET_NULL,
                                verbose_name='Группа',
                                related_name='group_containers',
                                null=True
                                )

    
    class Meta:
        verbose_name = 'Контейнер сообщений группы'
        verbose_name_plural = 'Контейнеры сообщений группы'


class DailyMessagesChannel(BaseDailyMessages):
    channel = models.ForeignKey(UsersChannel,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Канал',
                                    related_name='channel_containers',
                                    null=True
                                )


    class Meta:
        verbose_name = 'Контейнер сообщений канала'
        verbose_name_plural = 'Контейнеры сообщений канала'


class UserGroupMessage(BaseUserMessage):
    user = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                verbose_name='Отправитель',
                                related_name='group_messages',
                                null=True
                                )
    container = models.ForeignKey(DailyMessagesGroup,
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
    container = models.ForeignKey(DailyMessagesChannel,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Контейнер',
                                    related_name='channel_messages',
                                    null=True
                                )


    class Meta:
        verbose_name = 'Сообщение канала'
        verbose_name_plural = 'Сообщения канала'
