from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    # TODO additional fields : chats, groups, public_channels, private_channels, . . .

    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
