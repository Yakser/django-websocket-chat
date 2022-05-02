from django.db import models
from sorl.thumbnail import get_thumbnail

from django.utils.html import mark_safe

from core.models import BaseWebsocketGroup


class Group(BaseWebsocketGroup):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
