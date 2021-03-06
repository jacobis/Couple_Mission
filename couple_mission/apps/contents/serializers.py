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
        fields = ('id', 'user', 'couple', 'album', 'image',
                  'description', 'comment_manager', 'created_at', 'updated_at')


class LetterSerializer(serializers.ModelSerializer):
    gender = serializers.CharField()
    created_at = LocalizedDateTimeField()
    updated_at = LocalizedDateTimeField()
    # todo

    class Meta:
        model = Letter
        fields = (
            'id', 'user', 'couple', 'receiver', 'content', 'already_read',
                  'paper_type', 'gender', 'created_at', 'updated_at')
