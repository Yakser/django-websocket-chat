from core.models import BaseWebsocketGroup
from django.db import models


class UsersChannel(BaseWebsocketGroup):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     image = self._meta.get_field('image')
    #     image.verbose_name = 'Изображение канала'
    #     image.help_text = 'Выберите изображение канала'

    image = models.ImageField(verbose_name='Изображение канала',
                              upload_to='uploads/groups_images',
                              null=True,
                              help_text='Выберите изображение канала')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
