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
from couple_mission.apps.uai.mission_handler import MissionHandler

# Project Libs
from couple_mission.libs.common.string import sanitize


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

    def retrieve(self, request, pk):
        album = PhotoAlbum.objects.get(pk=pk)
        photos = Photo.objects.filter(album=album)
        serializer = PhotoSerializer(photos, many=True)

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        couple = CoupleController.get_couple(request.user)

        title = request.DATA.get('title')
        title = sanitize(title)

        photo_album = PhotoAlbum.objects.create(
            couple=couple, title=title)

        return Response({'success': True, 'data': {'photo_album_pk': photo_album.pk}}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        couple = CoupleController.get_couple(request.user)
        photo_album = PhotoAlbum.objects.get(pk=pk)
        serializer = PhotoAlbumSerializer(photo_album)
        return Response({'success': True, 'data': {'title': serializer.data['title']}}, status=status.HTTP_200_OK)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        couple_object = CoupleController.get_couple(request.user)
        photos = Photo.objects.filter(couple=couple_object)
        serializer = PhotoSerializer(photos, many=True)

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        couple = CoupleController.get_couple(request.user)
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        couple = CoupleController.get_couple(user)

        try:
            album_pk = request.DATA.get('album')
            album = PhotoAlbum.objects.get(pk=album_pk)
        except:
            album = None

        try:
            image = request.FILES.get('image')
        except:
            return Response({'success': False, 'message': _(u'사진 업로드 실패')}, status=status.HTTP_400_BAD_REQUEST)

        try:
            description = request.DATA.get('description')
            description = sanitize(description)
        except:
            description = None

        photo = Photo.objects.create(
            user=user, couple=couple, album=album, image=image, description=description)

        mission_handler = MissionHandler(user)
        mission_handler.new_cleared_missions()

        return Response({'success': True, 'data': {'photo_pk': photo.pk}}, status=status.HTTP_200_OK)

    @action(methods=['POST'])
    def comment(self, request, pk=None):
        user = request.user
        photo = Photo.objects.get(pk=pk)
        content = request.DATA.get('content')
        content = sanitize(content)

        comment = Comment.objects.create(
            comment_manager=photo.comment_manager, user=user, content=content)

        return Response({'success': True, 'data': {'comment_pk': comment.pk}}, status=status.HTTP_201_CREATED)


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        couple_object = CoupleController.get_couple(request.user)
        letters = Letter.objects.filter(couple=couple_object)
        serializer = LetterSerializer(letters, many=True)

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        couple = CoupleController.get_couple(request.user)
        letter = Letter.objects.get(pk=pk)

        if letter.user != request.user and not letter.already_read:
            letter.already_read = True
            letter.save()

        sender = letter.user.get_full_name()
        receiver = letter.receiver.get_full_name()
        content = letter.content
        paper_type = letter.paper_type
        comments = letter.comment_manager.comments.all()
        updated_at = letter.updated_at
        comments_serializer = CommentSerializer(comments, many=True)

        letter_data = {'sender': sender, 'receiver': receiver,
                       'content': content, 'updated_at': updated_at, 'paper_type': paper_type}

        return Response({'success': True, 'data': {'letter': letter_data, 'comments': comments_serializer.data}}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = request.user
        couple = CoupleController.get_couple(user)
        receiver = CoupleController.get_partner(couple, user)
        content = request.DATA.get('content')
        content = sanitize(content)
        paper_type = request.DATA.get('paper_type')
        if not paper_type:
            paper_type = Letter.PLAIN
        else:
            try:
                paper_type = int(paper_type)
            except:
                message = _(u'편지지 타입이 올바르지 않습니다.')
                return Response({'success': False, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

        letter = Letter.objects.create(
            user=user, couple=couple, receiver=receiver, content=content, paper_type=paper_type)

        mission_handler = MissionHandler(user)
        mission_handler.new_cleared_missions()

        return Response({'success': True, 'data': {'letter_pk': letter.pk}}, status=status.HTTP_201_CREATED)
