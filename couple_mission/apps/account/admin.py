from django.contrib import admin
from django.contrib.auth.models import User

# Project
from couple_mission.apps.account.models import UserProfile


class AdminUserProfile(admin.ModelAdmin):
    list_display = ('user', 'birthdate', )

admin.site.register(UserProfile, AdminUserProfile)