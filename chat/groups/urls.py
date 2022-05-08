from django.urls import path

from groups.views import (ClearGroupMessagesConfirmView,
                          ClearGroupMessagesView, CreateGroupView,
                          GroupsListView, GroupsView)

app_name = 'groups'

urlpatterns = [
    path('to/<slug:group_slug>/',
         GroupsView.as_view(),
         name='group'),
    path('create/',
         CreateGroupView.as_view(),
         name='create'),
    path('clear_messages_confirm/<slug:group_slug>/',
         ClearGroupMessagesConfirmView.as_view(),
         name='clear_messages_confirm'),
    path('clear_messages/<slug:group_slug>/',
         ClearGroupMessagesView.as_view(),
         name='clear_messages'),
    path('',
         GroupsListView.as_view(),
         name='groups_list'),
]
