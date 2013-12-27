from django.contrib import admin

# Project
from couple_mission.apps.uai.models import Badge, Title


class AdminBadge(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')


class AdminTitle(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Badge, AdminBadge)
admin.site.register(Title, AdminTitle)
