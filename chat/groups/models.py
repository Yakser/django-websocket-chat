from core.models import BaseWebsocketGroup


class Group(BaseWebsocketGroup):
    """
    Модель Группы. Наследуется от абстрактной модели BaseWebsocketGroup 
    """
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
