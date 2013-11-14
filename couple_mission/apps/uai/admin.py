from django.contrib import admin

# Project
from couple_mission.apps.uai.models import Mission, Badge, Title


class AdminMission(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'image', 'point')

class AdminBadge(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

class AdminTitle(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Mission, AdminMission)
admin.site.register(Badge, AdminBadge)
admin.site.register(Title, AdminTitle)