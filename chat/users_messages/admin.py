from django.contrib import admin
from users_messages.models import UserMessage


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'datetime')
