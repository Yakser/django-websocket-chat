from django.contrib import admin

from users_messages.models import (DailyChannelMessages, DailyChatMessages,
                                   DailyGroupMessages, UserChannelMessage,
                                   UserChatMessage, UserGroupMessage)


@admin.register(DailyChatMessages)
class DailyChatMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date',)


@admin.register(DailyGroupMessages)
class DailyGroupMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date',)


@admin.register(DailyChannelMessages)
class DailyChannelMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date',)


@admin.register(UserGroupMessage)
class UserGroupMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'time')


@admin.register(UserChannelMessage)
class UserChannelMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'time')


@admin.register(UserChatMessage)
class UserChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'time')
