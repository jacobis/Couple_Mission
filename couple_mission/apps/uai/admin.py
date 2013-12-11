from django.contrib import admin

# Project
from couple_mission.apps.uai.models import MissionCategory, Mission, Badge, Title


class AdminMissionCategory(admin.ModelAdmin):
    list_display = ('id', 'name')


class AdminMission(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'description', 'image', 'point')


class AdminBadge(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')


class AdminTitle(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(MissionCategory, AdminMissionCategory)
admin.site.register(Mission, AdminMission)
admin.site.register(Badge, AdminBadge)
admin.site.register(Title, AdminTitle)
