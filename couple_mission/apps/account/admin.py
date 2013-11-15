from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project
from couple_mission.apps.account.models import UaiUser, UserProfile

class AdminUserProfile(admin.ModelAdmin):
    list_display = ('user', 'birthdate', )

admin.site.register(UaiUser)
admin.site.register(UserProfile, AdminUserProfile)