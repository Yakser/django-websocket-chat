from django.contrib import admin
from users_messages.models import UserMessage, DailyMessages


@admin.register(DailyMessages)
class DailyMessagesAdmin(admin.ModelAdmin):
    list_display = ('date')


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'datetime')
