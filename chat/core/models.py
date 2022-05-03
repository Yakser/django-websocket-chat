import datetime
from django.db import models
from django.contrib.auth import get_user_model

from sorl.thumbnail import get_thumbnail

from django.utils.html import mark_safe


User = get_user_model()


class BaseUserMessage(models.Model):
    text = models.TextField(max_length=1024,
                            verbose_name='Текст')
    time = models.TimeField(verbose_name='Время отправки', null=True, default=datetime.datetime.now())

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user_id} {self.datetime}"


class BaseWebsocketGroup(models.Model):
    slug = models.SlugField(verbose_name='Идентификатор',
                            help_text='Используйте буквы, цифры или @/./+/-/_ ',
                            max_length=100,
                            unique=True,
                            primary_key=True, 
                            default='None')

    # TODO messages, owner_id, members

    name = models.CharField(verbose_name='Название',
                            max_length=150,
                            help_text='Введите название, длина до 150 символов',
                            default='Default group name')

    image = models.ImageField(verbose_name='Изображение группы',
                              upload_to='uploads/groups_images',
                              null=True,
                              help_text='Выберите изображение группы')

    def get_image_x256(self):
        return get_thumbnail(self.image,
                             '256',
                             quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50"')
        return 'Нет изображения'

    image_tmb.short_description = 'Изображение'
    image_tmb.allow_tags = True

    class Meta:
        abstract = True

    def __str__(self):
        return self.name[:15]


class BaseDailyMessages(models.Model):
    date = models.DateField(verbose_name='Дата создания', 
                            null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.date
