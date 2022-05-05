from django.contrib import admin

from .models import (DailyChannelMessages, DailyGroupMessages,
                     UserChannelMessage, UserGroupMessage)


@admin.register(DailyGroupMessages)
class DailyGroupMessagesAdmin(admin.ModelAdmin):
    list_display = ('date',)


@admin.register(DailyChannelMessages)
class DailyChannelMessagesAdmin(admin.ModelAdmin):
    list_display = ('date',)


@admin.register(UserGroupMessage)
class UserGroupMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'time')


@admin.register(UserChannelMessage)
class UserChannelMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'time')
