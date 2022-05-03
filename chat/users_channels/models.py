from core.models import BaseWebsocketGroup


class UsersChannel(BaseWebsocketGroup):
    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
