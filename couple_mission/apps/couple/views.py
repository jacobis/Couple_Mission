# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import parser

from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.couple.models import Couple, CoupleDday
from couple_mission.apps.couple.serializers import CoupleSerializer, CoupleDdaySerializer
from couple_mission.apps.couple.controller import CoupleController
from couple_mission.apps.uai.mission_handler import OneTimeMissionHandler
from couple_mission.apps.account.models import UserProfile

# Project Libs
from couple_mission.libs.common.string import sanitize
from couple_mission.libs.utils.datetime import normalize
from couple_mission.libs.permissions import IsOwnerOrCoupleOnly


class CoupleViewSet(viewsets.ModelViewSet):
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer
    permission_classes = (IsOwnerOrCoupleOnly,)

    def retrieve(self, reqeust, pk=None):
        couple = Couple.objects.get(pk=pk)

        # Partner detail
        partner_a_json = {}
        partner_b_json = {}
        partner_a = couple.partner_a
        partner_b = couple.partner_b
        partner_a_name = partner_a.last_name + partner_a.first_name
        partner_a_image = partner_a.userprofile.image
        partner_a_birthdate = partner_a.userprofile.birthdate
        partner_b_name = partner_b.last_name + partner_b.first_name
        partner_b_image = partner_b.userprofile.image
        partner_b_birthdate = partner_b.userprofile.birthdate
        partner_a_json['name'] = partner_a_name
        partner_a_json[
            'image'] = partner_a_image.url if partner_a_image else ''
        partner_a_json['birthdate'] = partner_a_birthdate
        partner_b_json['name'] = partner_b_name
        partner_b_json[
            'image'] = partner_b_image.url if partner_b_image else ''
        partner_b_json['birthdate'] = partner_b_birthdate

        image = couple.image.url if couple.image else ''
        first_date = couple.first_date

        return Response({'success': True,
                        'data': {'partner_a': partner_a_json, 'partner_b': partner_b_json, 'first_date': first_date, 'image': image}}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        couple = Couple.objects.get(pk=pk)
        image = request.FILES.get('image', None)
        first_date = request.DATA.get('first_date', None)

        if image is not None:
            couple.image = image

        if first_date is not None:
            try:
                first_date = parser.parse(first_date)
                couple.first_date = first_date
            except:
                return Response({'success': False, 'type': 'first_date', 'message': _(u'사귄날의 형식이 잘못 되었습니다.')}, status=status.HTTP_400_BAD_REQUEST)

        couple.save()

        return Response({'success': True}, status=status.HTTP_200_OK)


class CoupleDdayViewSet(viewsets.ModelViewSet):
    queryset = CoupleDday.objects.all()
    serializer_class = CoupleDdaySerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        couple_object = CoupleController.get_couple(request.user)
        couple_ddays = CoupleDday.objects.filter(couple=couple_object)
        serializer = CoupleDdaySerializer(couple_ddays, many=True)

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        couple = CoupleController.get_couple(request.user)
        request.DATA['couple'] = couple.pk
        request.DATA['title'] = sanitize(request.DATA['title'])

        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
