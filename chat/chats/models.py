from django.contrib.auth import get_user_model
from django.db import models

from django.db.models import Q
from django.db.models.query import QuerySet


User = get_user_model()


class ChatManager(models.Manager):
    def get_chat_by_users(self,  first_user: User, second_user: User) -> QuerySet:
        return Chat.objects.filter(Q(first_user=first_user) & Q(second_user=second_user) |
                                   Q(first_user=second_user) & Q(second_user=first_user))


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

    def check_if_user_is_member(self, user: User) -> bool:
        """
        Проверяет, является ли пользователь участником чата

        Args:
            user (User): пользователь

        Returns:
            bool
        """
        return self.first_user.id == user.id or self.second_user.id == user.id

    objects = ChatManager()

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f"Chat<{self.id}>"
