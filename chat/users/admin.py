from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe

from users.models import Profile

User = get_user_model()


class ProfileInlined(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (ProfileInlined, )
    list_display = ('email', 'username', 'is_staff',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
