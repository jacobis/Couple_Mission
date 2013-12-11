# -*- coding: utf-8 -*-

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
from couple_mission.apps.couple.models import Couple, CoupleMission
from couple_mission.apps.couple.serializers import CoupleSerializer
from couple_mission.apps.uai.views import Mission

# Project Libs
from couple_mission.libs.common.string import sanitize


class CoupleViewSet(viewsets.ModelViewSet):
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer

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
