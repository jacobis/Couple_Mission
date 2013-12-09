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
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        couple_object = CoupleController.get_couple(request.user)
        photo_albums = PhotoAlbum.objects.filter(couple=couple_object)
        serializer = PhotoAlbumSerializer(photo_albums, many=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user
        couple = CoupleController.get_couple(request.user)

        title = request.DATA.get('title')

        photo_album = PhotoAlbum.objects.create(
            user=user, couple=couple, title=title)

        return Response({'success': True, 'data': {'photo_album_pk': photo_album.pk}}, status=status.HTTP_200_OK)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        couple_object = CoupleController.get_couple(request.user)
        photos = Photo.objects.filter(couple=couple_object)
        serializer = PhotoSerializer(photos, many=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user
        couple = CoupleController.get_couple(request.user)

        try:
            album_pk = request.DATA.get('album')
            album = PhotoAlbum.objects.get(pk=album_pk)

        except Exception as e:
            print e
            return Response({'success': False, 'message': _(u'앨범')}, status=status.HTTP_400_BAD_REQUEST)

        try:
            image = request.FILES.get('image')
        except:
            return Response({'success': False, 'message': _(u'사진 업로드 실패')}, status=status.HTTP_400_BAD_REQUEST)
        description = request.DATA.get('description')

        photo = Photo.objects.create(
            user=user, couple=couple, album=album, image=image, description=description)

        return Response({'success': True, 'data': {'photo_pk': photo.pk}}, status=status.HTTP_200_OK)


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)
        user = request.user
        couple_id = request.couple_id
        couple = Couple.objects.get(id=couple_id)

        self.pre_save(serializer.object)
        self.object = serializer.save(force_insert=True)
        self.post_save(self.object, created=True)
        headers = self.get_success_headers(serializer.data)

        return Response({'success': True}, status=status.HTTP_201_CREATED)
