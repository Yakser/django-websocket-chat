from core.models import BaseWebsocketGroup
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UsersChannel(BaseWebsocketGroup):
    """
    Модель Канала. Наследуется от абстрактной модели BaseWebsocketGroup. 
    
    """
    
    image = models.ImageField(verbose_name='Изображение канала',
                              upload_to='uploads/groups_images',
                              null=True,
                              help_text='Выберите изображение канала')
    owner = models.ForeignKey(User,
                              verbose_name='Владелец',
                              related_name='owner_users_channels',
                              on_delete=models.SET_NULL,
                              null=True)

    group_members = models.ManyToManyField(User,
                                           verbose_name='Участники',
                                           related_name='users_channels'
                                           )

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
