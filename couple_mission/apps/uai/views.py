# -*- coding: utf-8 -*-

import datetime

from django.shortcuts import render
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.uai.models import Badge, Title
from couple_mission.apps.couple.models import CoupleMission
from couple_mission.apps.uai.serializers import MissionCategorySerializer, BadgeSerializer, TitleSerializer

# Project Libs
from couple_mission.libs.common.string import sanitize

from couple_mission.apps.uai.mission_handler import MissionHandler


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


def main_index(request):
    return render(request, 'index.html')
