from django.contrib import admin
from django.contrib.auth.models import User

# Project
from couple_mission.apps.contents.models import Comment, PhotoAlbum, Photo, Letter
from couple_mission.apps.couple.models import Couple


class AdminPhotoAlbum(admin.ModelAdmin):
    list_display = ('id', 'couple', 'title')


class AdminPhoto(admin.ModelAdmin):
    list_display = (
        'user', 'couple', 'album', 'image', 'description')


class AdminLetter(admin.ModelAdmin):
    list_display = ('user', 'couple', 'content', 'already_read')


class AdminComment(admin.ModelAdmin):
    list_display = ('user', 'content')

admin.site.register(PhotoAlbum, AdminPhotoAlbum)
admin.site.register(Photo, AdminPhoto)
admin.site.register(Letter, AdminLetter)
admin.site.register(Comment, AdminComment)
