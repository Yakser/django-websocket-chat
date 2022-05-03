from django.contrib import admin
from .models import (DailyMessagesGroup, 
                        DailyMessagesChannel, 
                        UserGroupMessage,
                        UserChannelMessage)


@admin.register(DailyMessagesGroup)
class DailyMessagesGroupAdmin(admin.ModelAdmin):
    list_display = ('date',)


@admin.register(DailyMessagesChannel)
class DailyMessagesChannelAdmin(admin.ModelAdmin):
    list_display = ('date',)


@admin.register(UserGroupMessage)
class UserGroupMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'time')


@admin.register(UserChannelMessage)
class UserChannelMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'time')
