from django.urls import path

from chats.views import (ChatRedirectOrCreateView, ChatsListView, ChatView,
                         ClearChatMessagesConfirmView, ClearChatMessagesView)

app_name = 'chats'

urlpatterns = [
    path('<int:chat_id>/',
         ChatView.as_view(),
         name='chat'),
    path('clear_messages_confirm/<slug:group_slug>/',
         ClearChatMessagesConfirmView.as_view(),
         name='clear_messages_confirm'),
    path('clear_messages/<slug:group_slug>/',
         ClearChatMessagesView.as_view(),
         name='clear_messages'),
    path('',
         ChatsListView.as_view(),
         name='chats_list'),
    path('redirect_or_create/',
         ChatRedirectOrCreateView.as_view(),
         name='redirect_or_create')
]
