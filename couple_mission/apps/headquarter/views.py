# -*- coding: utf-8 -*-

# Django
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Permissions
from couple_mission.libs.permissions import IsAdminUserOrReadOnly

# Project
from couple_mission.apps.headquarter.models import Notice
from couple_mission.apps.headquarter.serializers import NoticeSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
