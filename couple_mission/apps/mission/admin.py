from django.contrib import admin

# Project
from couple_mission.apps.couple.models import Couple
from couple_mission.apps.mission.models import MissionCategory, MissionType, Mission, UserMission


class AdminMissionCategory(admin.ModelAdmin):
    list_display = ('id', 'identity', 'name')


class AdminMissionType(admin.ModelAdmin):
    list_display = ('id', 'identity', 'name')


class AdminMission(admin.ModelAdmin):
    list_display = ('id', 'category', 'title',
                    'description1', 'description2', 'image', 'question', 'answer', 'point', 'is_active')


class AdminUserMission(admin.ModelAdmin):
    list_display = ('id', 'mission', 'user', 'couple', 'status')


admin.site.register(MissionCategory, AdminMissionCategory)
admin.site.register(MissionType, AdminMissionType)
admin.site.register(Mission, AdminMission)
admin.site.register(UserMission, AdminUserMission)
