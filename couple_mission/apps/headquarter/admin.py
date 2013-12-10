from django.contrib import admin

# Project
from couple_mission.apps.headquarter.models import Notice


class AdminNotice(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

admin.site.register(Notice, AdminNotice)
