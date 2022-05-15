from django.urls import path

from chats.views import (ChatRedirectOrCreateView, ChatsListView, ChatView,
                         ClearChatMessagesConfirmView, ClearChatMessagesView)

app_name = 'chats'

urlpatterns = [
    path('<int:chat_id>/',
         ChatView.as_view(),
         name='chat'),
    path('clear_messages_confirm/<int:chat_id>/',
         ClearChatMessagesConfirmView.as_view(),
         name='clear_messages_confirm'),
    path('clear_messages/<int:chat_id>/',
         ClearChatMessagesView.as_view(),
         name='clear_messages'),
    path('',
         ChatsListView.as_view(),
         name='chats_list'),
    path('redirect_or_create/',
         ChatRedirectOrCreateView.as_view(),
         name='redirect_or_create')
]
