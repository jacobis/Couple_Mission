# -*- coding: utf-8 -*-

import datetime
import platform

from django.http import HttpResponseRedirect
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
from couple_mission.apps.uai.serializers import BadgeSerializer, TitleSerializer

# Project Libs
from couple_mission.libs.common.string import sanitize


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


def main_index(request):
    return render(request, 'index.html')


def app_download(request):
    user_agent = request.user_agent.os.family
    print user_agent
    if user_agent == 'Android':
        return HttpResponseRedirect("https://play.google.com/apps/testing/nalebe.couplemission.ui")
    else:
        return render(request, 'app_download.html')
