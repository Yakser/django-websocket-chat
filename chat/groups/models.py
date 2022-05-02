from django.db import models
from sorl.thumbnail import get_thumbnail

from django.utils.html import mark_safe


class Group(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=150,
                            help_text='Введите название, длина до 150 символов',
                            default='Default group name')

    image = models.ImageField(verbose_name='Изображение группы',
                              upload_to='uploads/',
                              null=True,
                              help_text='Выберите изображение группы')

    def get_image_x1280(self):
        return get_thumbnail(self.preview,
                             '1280',
                             quality=51)

    def image_tmb(self):
        if self.preview:
            return mark_safe(f'<img src="{self.preview.url}" width="50"')
        return 'Нет изображения'

    image_tmb.short_description = 'Изображение'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name[:15]
