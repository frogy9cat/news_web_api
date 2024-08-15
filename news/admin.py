from django.contrib import admin
from django.contrib.auth.models import Group

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_display_links = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')


    # def get_raw_readonly(self, obj):
    #     return f'{obj.created_at}'


admin.site.register(News, NewsAdmin)

admin.site.unregister(Group)