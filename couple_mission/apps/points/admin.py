from django.contrib import admin

# Project
from couple_mission.apps.points.models import Points
from couple_mission.apps.account.models import UaiUser
from couple_mission.apps.couple.models import Couple, CoupleMission


class AdminPoints(admin.ModelAdmin):
    list_display = ('couple', 'points')

admin.site.register(Points, AdminPoints)