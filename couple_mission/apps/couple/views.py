# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.couple.models import Couple
from couple_mission.apps.couple.serializers import CoupleSerializer

class CoupleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer