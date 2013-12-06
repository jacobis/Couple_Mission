# -*- coding: utf-8 -*-

# Django
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# RESE Framework Authentication & Permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Project
from couple_mission.apps.couple.models import Couple
from couple_mission.apps.contents.models import Comment, PhotoAlbum, Photo, Letter
from couple_mission.apps.contents.serializers import CommentSerializer, PhotoAlbumSerializer, PhotoSerializer, LetterSerializer
from couple_mission.apps.couple.controller import CoupleController


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PhotoAlbumViewSet(viewsets.ModelViewSet):
    queryset = PhotoAlbum.objects.all()
    serializer_class = PhotoAlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)
        user = request.user
        raise ValueError(123)
        couple_id = request.couple_id
        couple = Couple.objects.get(id=couple_id)

        self.pre_save(serializer.object)
        self.object = serializer.save(force_insert=True)
        self.post_save(self.object, created=True)
        headers = self.get_success_headers(serializer.data)

        return Response({'success': True}, status=status.HTTP_201_CREATED)
