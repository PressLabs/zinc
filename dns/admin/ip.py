from django.contrib import admin

from ..models import IP


@admin.register(IP)
class IPAdmin(admin.ModelAdmin):
    list_display = ['ip', 'location', 'server_name']