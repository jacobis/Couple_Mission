from django.contrib.auth.models import User
from couple_mission.apps.contents.models import Comment, PhotoAlbum, Photo, Letter

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

class PhotoAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoAlbum

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo

class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
