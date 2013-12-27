# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from couple_mission.apps.mission.models import MissionCategory, Mission, UserMission, MissionType
from couple_mission.apps.mission.serializers import UserMissionSerializer
from couple_mission.apps.couple.controller import CoupleController


class UserMissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mission.active.all()
    serializer_class = UserMissionSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):

        # Mission Category Setup
        category = request.GET.get("category", "DM")
        category = category.upper()
        if category not in ["DM", "LM", "CM", "EM"]:
            category = "DM"

        category = MissionCategory.objects.get(identity=category)

        # UserMission Get or Create

        user = request.user
        couple = CoupleController.get_couple(user)
        missions = Mission.active.filter(category=category)

        for mission in missions:
            UserMission.objects.get_or_create(
                user=user, couple=couple, mission=mission)

        page = self.paginate_queryset(missions)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(missions, many=True)

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
