from django.contrib import admin

# Project
from couple_mission.apps.contents.models import Comment, PhotoAlbum, Photo, Letter
from couple_mission.apps.account.models import UaiUser
from couple_mission.apps.couple.models import Couple


class AdminPhoto(admin.ModelAdmin):
    list_display = ('user', 'couple', 'album', 'image', 'description', 'comment')

class AdminLetter(admin.ModelAdmin):
    list_display = ('user', 'couple', 'content', 'reading')

class AdminComment(admin.ModelAdmin):
    list_display = ('user', 'couple', 'content')

admin.site.register(Photo, AdminPhoto)
admin.site.register(Letter, AdminLetter)
admin.site.register(Comment, AdminComment)