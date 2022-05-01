from django.urls import path

from groups.views import GroupsView

app_name = 'groups'
urlpatterns = [
    path('<slug:group_name>/', GroupsView.as_view(), name='group'),
]
