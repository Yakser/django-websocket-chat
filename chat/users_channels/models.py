from django.db import models
from sorl.thumbnail import get_thumbnail

from django.utils.html import mark_safe

from core.models import BaseWebsocketGroup


class UsersChannel(BaseWebsocketGroup):
    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
