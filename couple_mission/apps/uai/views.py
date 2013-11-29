# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.uai.models import MissionCategory, Mission, Badge, Title
from couple_mission.apps.uai.serializers import MissionCategorySerializer, MissionSerializer, BadgeSerializer, TitleSerializer


class MissionCategoryViewSet(viewsets.ModelViewSet):
    queryset = MissionCategory.objects.all()
    serializer_class = MissionCategorySerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
