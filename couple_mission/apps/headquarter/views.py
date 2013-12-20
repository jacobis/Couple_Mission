# -*- coding: utf-8 -*-

# Django
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Permissions
from couple_mission.libs.permissions import IsAdminUserOrReadOnly

# Project
from couple_mission.apps.headquarter.models import Notice
from couple_mission.apps.headquarter.serializers import NoticeSerializer

# Project Libs
from couple_mission.libs.common.string import sanitize


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
