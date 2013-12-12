# -*- coding: utf-8 -*-

import re
import urllib
from dateutil import parser

# Django
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import status, parsers, renderers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.decorators import action

# REST Framework Authentication & Permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Project
from couple_mission.apps.account.models import UserProfile
from couple_mission.apps.account.serializers import UserSerializer, UserProfileSerializer, AuthTokenSerializer
from couple_mission.apps.couple.controller import CoupleController

# Project Libs
from couple_mission.libs.common.string import sanitize


class UserViewSet(viewsets.ModelViewSet):

    """
    Users list, create, retrieve, update, destroy
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            token = Token.objects.get(user=self.object)

            return Response(
                {'success': True, 'message': _(u'Sign up success.'), 'token': token.key}, status=status.HTTP_201_CREATED,
                headers=headers)

        return Response({'success': False, 'message': _(u'%s') % serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    """
    유저가 Create 될때 User id와 매칭되는 Token, UserProfile 생성
    """
    @receiver(post_save, sender=User)
    def initialize_user(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
            UserProfile.objects.create(user=instance)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects .all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def __validate__(self, gender, birthdate, first_date):

        error_dic = {}

        if gender is not None:
            if gender.upper() not in ['M', 'F']:
                error_dic['type'] = 'gender'
                error_dic['message'] = _(u'성별의 형식이 잘못 되었습니다.')
                return error_dic

        if birthdate is not None:
            try:
                parser.parse(birthdate)
            except:
                error_dic['type'] = 'birthdate'
                error_dic['message'] = _(u'생년월일의 형식이 잘못 되었습니다.')
                return error_dic

        if first_date is not None:
            try:
                parser.parse(first_date)
            except:
                error_dic['type'] = 'first_date'
                error_dic['message'] = _(u'사귄날의 형식이 잘못 되었습니다.')
                return error_dic

        return None

    def update(self, request, pk=None):
        # 필드들의 변경은 가능

        first_name = request.DATA.get('first_name', None)
        if first_name is not None:
            first_name = sanitize(first_name)
        last_name = request.DATA.get('last_name', None)
        if last_name is not None:
            last_name = sanitize(last_name)
        gender = request.DATA.get('gender', None)
        birthdate = request.DATA.get('birthdate', None)
        first_date = request.DATA.get('first_date', None)

        image = request.FILES.get('image', None)

        error_dic = self.__validate__(
            gender, birthdate, first_date)

        if error_dic:
            print error_dic
            error_type = error_dic['type']
            message = error_dic['message']
            return Response({'success': False, 'type': error_dic['type'], 'message': error_dic['message']}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        userprofile = user.userprofile
        couple = CoupleController.get_couple(user)

        if first_name is not None:
            user.first_name = sanitize(first_name)

        if last_name is not None:
            user.last_name = sanitize(last_name)

        if gender is not None:
            userprofile.gender = gender

        if birthdate is not None:
            userprofile.birthdate = parser.parse(birthdate).date()

        if first_date is not None and couple:
            couple.first_date = parser.parse(first_date).date()

        if image is not None:
            userprofile.image = image

        user.save()
        userprofile.save()
        if couple:
            couple.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(methods=['PUT'])
    def starter(self, request, pk=None):
        userprofile = request.user.userprofile
        userprofile.starter = True
        userprofile.save()

        return Response({'success': True}, status=status.HTTP_200_OK)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    model = Token

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.DATA)

        if serializer.is_valid():
            token, created = Token.objects.get_or_create(
                user=serializer.object['user'])
            return Response({'success': True, 'token': token.key})
        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Me(APIView):

    def get(self, request):
        couple = CoupleController.get_couple(request.user)
        couple_id = couple.pk if couple else 0
        user_id = request.user.pk
        starter = request.user.userprofile.starter

        return Response({'success': True, 'couple_id': couple_id, 'user_id': user_id, 'starter': starter}, status=status.HTTP_200_OK)


obtain_auth_token = ObtainAuthToken.as_view()
me = Me.as_view()
