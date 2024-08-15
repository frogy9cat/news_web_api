from django.contrib import admin

from .models import TelegramUsers


class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'telegram_id', 'phone_number', 'created_at', 'updated_at')
    list_display_links = ('full_name', 'username', 'telegram_id', 'phone_number')
    search_fields = ('full_name', 'username', 'telegram_id', 'phone_number')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('created_at',)



admin.site.register(TelegramUsers, TelegramUsersAdmin)