from django.contrib import admin


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb')
