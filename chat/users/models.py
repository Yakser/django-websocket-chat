from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    biography = models.TextField(
        verbose_name='О себе',
        max_length=500,
        unique=False,
        null=True,
        help_text='Немного расскажите о себе'
    )

    image = models.ImageField(verbose_name='Изображение пользователя',
                              upload_to='uploads/users_images',
                              null=True,
                              help_text='Выберите изображение')

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

    # TODO additional fields : chats, groups, public_channels, private_channels, . . .

    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
