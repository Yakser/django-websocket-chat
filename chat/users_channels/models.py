from django.db import models
from sorl.thumbnail import get_thumbnail

from django.utils.html import mark_safe

from core.models import BaseWebsocketGroup


class UsersChannel(BaseWebsocketGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image = self._meta.get_field('image')
        image.verbose_name = 'Изображение канала'
        image.help_text = 'Выберите изображение канала'

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'