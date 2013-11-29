from django.contrib import admin

# Project
from couple_mission.apps.couple_request.models import CoupleRequest

class AdminCoupleRequest(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_sender', 'request_receiver', 'connected')

admin.site.register(CoupleRequest, AdminCoupleRequest)