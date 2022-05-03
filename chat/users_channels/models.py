from core.models import BaseWebsocketGroup
from django.db import models


class UsersChannel(BaseWebsocketGroup):
    image = models.ImageField(verbose_name='Изображение канала',
                              upload_to='uploads/groups_images',
                              null=True,
                              help_text='Выберите изображение канала')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
