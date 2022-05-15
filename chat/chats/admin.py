from django.contrib import admin

from chats.models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_user', 'second_user')
    list_display_links = ('id', 'first_user', 'second_user')
