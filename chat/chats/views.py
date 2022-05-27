from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.handlers.asgi import ASGIRequest
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic.base import RedirectView, TemplateView
from users_messages.models import DailyChatMessages
from websockets.connection_types import CHATS_CONNECTION

from chats.models import Chat

User = get_user_model()


@method_decorator(login_required, name='dispatch')
class ChatView(TemplateView):
    """
    Отображает модель Chat - список сообщений, панель редактирования и удаления чата,
    поле отправки сообщения

    Context:
        connection_type (str): тип подключения к вебсокетам
        is_member (bool): флаг, указывающий является ли пользователь участником чата
        user (User): экземпляр класса User
        chat (Chat): экземпляр класса Chat
        messages (UserChatMessage[]): сообщения чата

    Template:
        template_name: 'chats/chat.html'

    """

    template_name = 'chats/chat.html'

    def get(self, request: ASGIRequest, chat_id: int, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user, chat_id))

    def get_context_data(self, user: User, chat_id: int, **kwargs):
        context = super().get_context_data(**kwargs)

        chat: Chat = get_object_or_404(Chat, pk=chat_id)

        context['connection_type'] = CHATS_CONNECTION
        context['chat'] = chat
        context['user'] = user
        context['is_member'] = False

        if chat.check_if_user_is_member(user):
            container, is_created = DailyChatMessages.objects.get_or_create(chat=chat)

            messages = container.get_messages()

            context['is_member'] = True
            context['chat'] = chat
            context['messages'] = messages

        return context


class ChatsListView(TemplateView):
    """
    Отображает список чатов (Chat)

    Context:
        chats (Chat[]): QuerySet содержащий экземпляры класса Chat

    Template:
        template_name: 'chats/chats_list.html'
    """

    template_name = 'chats/chats_list.html'

    def get(self, request: ASGIRequest, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user))

    def get_context_data(self, user: User, **kwargs):
        context = super().get_context_data(**kwargs)

        # получаем чаты пользователя
        chats: QuerySet = user.first_user_chats.all() | user.second_user_chats.all()

        context['chats'] = chats
        return context


class ChatRedirectOrCreateView(RedirectView):
    """
    Перенаправляет пользователя на страницу чата.
    Если чата не существует, то он создается и пользователь также перенаправляется в чат.

    Pattern:
        pattern_name: 'chats:chat'

    """
    permanent = False
    query_string = True
    pattern_name = 'chats:chat'

    def get_redirect_url(self, *args, **kwargs):
        first_username = self.request.user.username
        second_username = self.request.GET.get('username')

        first_user = get_object_or_404(User, username=first_username)
        second_user = get_object_or_404(User, username=second_username)

        chats: QuerySet = Chat.objects.get_chat_by_users(first_user, second_user)
        if chats:
            chat = chats.first()
        else:
            chat = Chat(first_user=first_user, second_user=second_user)
            chat.save()

        return super().get_redirect_url(chat_id=chat.id)


@method_decorator(login_required, name='dispatch')
class ClearChatMessagesConfirmView(TemplateView):
    """
    Отображает модальное окно с подтверждением удаления истории сообщений

    Context:
        chat (Chat): экземпляр класса Chat

    Template:
        template_name: 'chats/clear_chat_messages_confirm.html'
    """

    template_name = 'chats/clear_chat_messages_confirm.html'

    def get(self, request: ASGIRequest, chat_id: int, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(chat_id))

    def get_context_data(self, chat_id: int, **kwargs):
        context = super().get_context_data(**kwargs)
        chat = get_object_or_404(Chat, pk=chat_id)
        context['chat'] = chat
        return context


@method_decorator(login_required, name='dispatch')
class ClearChatMessagesView(TemplateView):
    """
    Отображает страницу с сообщением об успешном удалении истории сообщений чата

    Context:
        chat (Chat): экземпляр класса Chat

    Template:
        template_name: 'chats/clear_chats_messages.html'
    """

    template_name = 'chats/clear_chats_messages.html'

    def get(self, request: ASGIRequest, chat_id: int, *args, **kwargs):
        chat: Chat = get_object_or_404(Chat, pk=chat_id)

        chat_container: DailyChatMessages = DailyChatMessages.objects.get(chat=chat)
        chat_container.chat_messages.all().delete()

        return render(request,
                      self.template_name,
                      self.get_context_data(chat_id))

    def get_context_data(self, chat_id: int, **kwargs):
        context = super().get_context_data(**kwargs)
        chat = get_object_or_404(Chat, pk=chat_id)
        context['chat'] = chat
        return context
