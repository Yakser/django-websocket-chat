from django.contrib import admin
from groups.models import Group


@admin.register(Group)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb')
