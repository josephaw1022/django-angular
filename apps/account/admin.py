
from django.contrib.auth.models import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name']
