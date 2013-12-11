from django.contrib.auth.models import User
from couple_mission.apps.contents.models import Comment, PhotoAlbum, Photo, Letter
from couple_mission.libs.common.field import LocalizedDateTimeField

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment


class PhotoAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoAlbum


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image_url')
    created_at = LocalizedDateTimeField()
    updated_at = LocalizedDateTimeField()

    class Meta:
        model = Photo
        fields = ('user', 'couple', 'album', 'image',
                  'description', 'created_at', 'updated_at')


class LetterSerializer(serializers.ModelSerializer):
    gender = serializers.CharField()
    created_at = LocalizedDateTimeField()
    updated_at = LocalizedDateTimeField()
    # todo

    class Meta:
        model = Letter
        fields = ('user', 'couple', 'comment_manager', 'receiver',
                  'content', 'already_read', 'paper_type', 'gender', 'created_at', 'updated_at')
