# -*- coding: utf-8 -*-

import datetime

from django.shortcuts import render

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.uai.models import MissionCategory, Mission, Badge, Title
from couple_mission.apps.couple.models import CoupleMission
from couple_mission.apps.uai.serializers import MissionCategorySerializer, MissionSerializer, BadgeSerializer, TitleSerializer

# Project Libs
from couple_mission.libs.common.string import sanitize

from couple_mission.apps.uai.mission_handler import MissionHandler


class MissionCategoryViewSet(viewsets.ModelViewSet):
    queryset = MissionCategory.objects.all()
    serializer_class = MissionCategorySerializer


class MissionView(viewsets.ReadOnlyModelViewSet):
    models = Mission
    # permission_classes = (IsAuthenticated,)


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class Mission():

    def letter_mission(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d 00:00')
        letters = Letter.objects.filter(updated_at__gte=date)
        if letters:
            mission = Mission.objects.get(id=1)
            mission.status = True
            return Response({'status': "Congratulation! You get 10 points."})


def mission_detail_view(request, mission_id):
    mission_handler = MissionHandler(request, mission_id)
    if not mission_handler.has_cleared():
        mission_result = mission_handler.do_mission()

    raise ValueError('end')


def main_index(request):
    return render(request, 'index.html')
