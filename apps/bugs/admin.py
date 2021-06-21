# Register your models here.

from django.contrib import admin
from .models import *


class BugAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "completed", "owner", "started"]


# Register your models here.
admin.site.register(Bug, BugAdmin)
