from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserMessage(models.Model):
    text = models.TextField(max_length=1024,
                            verbose_name='Текст')
    datetime = models.DateTimeField()
    user = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                verbose_name='Отправитель',
                                related_name='messages',
                                null=True
                                )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f"{self.user_id} {self.datetime}"
