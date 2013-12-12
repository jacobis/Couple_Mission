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
from couple_mission.apps.couple.models import Couple, CoupleMission
from couple_mission.apps.couple.serializers import CoupleSerializer, CoupleMissionSerializer
from couple_mission.apps.uai.models import Mission, MissionCategory
from couple_mission.apps.couple.controller import CoupleController
from couple_mission.apps.uai.mission_handler import OneTimeMissionHandler

# Project Libs
from couple_mission.libs.common.string import sanitize
from couple_mission.libs.utils.datetime import normalize


class CoupleViewSet(viewsets.ModelViewSet):
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, reqeust, pk=None):
        couple = Couple.objects.get(pk=pk)
        partner_a_json = {}
        partner_b_json = {}
        partner_a = couple.partner_a
        partner_b = couple.partner_b
        partner_a_name = partner_a.last_name + partner_a.first_name
        partner_a_image = partner_a.userprofile.image
        partner_a_birthdate = partner_a.userprofile.birthdate
        partner_b_name = partner_b.last_name + partner_b.last_name
        partner_b_image = partner_b.userprofile.image
        partner_b_birthdate = partner_b.userprofile.birthdate
        partner_a_json['name'] = partner_a_name
        partner_a_json[
            'image'] = partner_a_image.url if partner_a_image else ''
        partner_a_json['birthdate'] = partner_a_birthdate
        partner_b_json['name'] = partner_b_name
        partner_b_json['image'] = partner_b_image if partner_b_image else ''
        partner_b_json['birthdate'] = partner_b_birthdate
        first_date = couple.first_date

        return Response({'success': True,
                        'data': {'partner_a': partner_a_json, 'partner_b': partner_b_json, 'first_date': first_date}}, status=status.HTTP_200_OK)

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


class CoupleMissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mission.active.all()
    serializer_class = CoupleMissionSerializer
    # permission_classes = (IsAuthenticated,)
    pass

    def list(self, request):
        category = request.GET.get("category", "DM")
        category_param = category.upper()
        if category_param not in ["DM", "LM", "CM"]:
            category_param = "DM"
        category = MissionCategory.objects.get(identity=category_param)
        couple = CoupleController.get_couple(request.user)
        missions = Mission.active.filter(category=category)
        ret_list = []
        for mission in missions:
            mission_json = {}
            couple_mission, created = CoupleMission.objects.get_or_create(
                couple=couple, mission=mission)
            mission_json['pk'] = couple_mission.pk
            mission_json['title'] = mission.title
            mission_json['description'] = mission.description
            mission_json['image'] = mission.image.url if mission.image else ''
            mission_json['point'] = mission.point
            mission_json['status'] = couple_mission.status
            mission_json['created_at'] = normalize(mission.created_at)
            mission_json['updated_at'] = normalize(mission.updated_at)

            ret_list.append(mission_json)

        return Response({'success': True, 'data': {'couple_missions': ret_list}}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        couple_mission = CoupleMission.objects.get(pk=pk)
        mission = couple_mission.mission

        mission_json = {}
        mission_json['pk'] = couple_mission.pk
        mission_json['title'] = mission.title
        mission_json['description'] = mission.description
        mission_json['image'] = mission.image.url if mission.image else ''
        mission_json['point'] = mission.point
        mission_json['status'] = couple_mission.status
        mission_json['created_at'] = normalize(mission.created_at)
        mission_json['updated_at'] = normalize(mission.updated_at)

        return Response({'success': True, 'data': {'couple_mission': mission_json}}, status=status.HTTP_200_OK)

    @action(methods=['POST'])
    def start_mission(self, request, pk=None):
        couple_mission = CoupleMission.objects.get(pk=pk)
        couple_mission.status = CoupleMission.DOING
        couple_mission.started_datetime = datetime.utcnow()
        couple_mission.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(methods=['POST'])
    def do_mission(self, request, pk=None):
        mission_handler = OneTimeMissionHandler(request, mission_id=pk)
        if not mission_handler.has_cleared() == CoupleMission.REWARDABLE:
            mission_result = mission_handler.do_mission()

            return Response({'success': mission_result}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'type': 'mission', 'message': _(u'이미 수행한 미션입니다.')})
