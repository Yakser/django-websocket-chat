from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    """
    Модель чат между двумя пользователями.    

    Attributes:
        first_user (User): первый участник чата
        second_user (User): второй участник чата

    """
    first_user = models.ForeignKey(User,
                                   verbose_name='Первый пользователь чата',
                                   related_name='first_user_chats',
                                   on_delete=models.CASCADE)
    second_user = models.ForeignKey(User,
                                    verbose_name='Второй пользователь чата',
                                    related_name='second_user_chats',
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f"Chat<{self.id}>"
