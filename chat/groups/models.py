from core.models import BaseWebsocketGroup


class Group(BaseWebsocketGroup):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
