from django.contrib import admin

from users_channels.models import UsersChannel


@admin.register(UsersChannel)
class UsersChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb', )
