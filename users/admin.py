from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth import get_user_model

from linemetals_api.settings import ADMIN_SITE_HEADER, ADMIN_SITE_TITLE

admin.AdminSite.site_header = ADMIN_SITE_HEADER
admin.AdminSite.site_title = ADMIN_SITE_TITLE

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'role', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
