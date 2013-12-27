from django.contrib import admin
from django.contrib.auth.models import User

# Project
from couple_mission.apps.points.models import Points


class AdminPoints(admin.ModelAdmin):
    list_display = ('couple', 'points')

admin.site.register(Points, AdminPoints)
