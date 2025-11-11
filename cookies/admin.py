from django.contrib import admin
from .models import Cookie


@admin.register(Cookie)
class CookieAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
