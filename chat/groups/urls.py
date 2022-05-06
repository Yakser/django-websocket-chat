from django.urls import path

from groups.views import CreateGroupView, GroupsListView, GroupsView

app_name = 'groups'

urlpatterns = [
    path('to/<slug:group_slug>/', GroupsView.as_view(), name='group'),
    path('create/', CreateGroupView.as_view(), name='create_group'),
    path('', GroupsListView.as_view(), name='groups_list'),
]
