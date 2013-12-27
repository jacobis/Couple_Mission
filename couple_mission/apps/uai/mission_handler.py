# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import parser

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from couple_mission.apps.mission.models import Mission, UserMission
from couple_mission.apps.couple.controller import CoupleController
from couple_mission.apps.contents.models import Photo, Letter


class MissionHandler():

    def __init__(self, user):
        if not isinstance(user, User):
            raise Exception('must pass User object.')

        self.user = user
        self.couple = CoupleController.get_couple(user)

    def new_cleared_missions(self):
        mission_pks = self.get_uncleared_missions()
        if mission_pks is None:
            return None
        new_cleared_missions = []
        for mission_pk in mission_pks:
            couple_mission = self.do_mission(mission_pk)
            if couple_mission.status == UserMission.REWARDABLE:
                new_cleared_missions.append(couple_mission)

        return new_cleared_missions

    def get_uncleared_missions(self):
        couple_missions = UserMission.objects.filter(
            couple=self.couple).exclude(status=UserMission.REWARDABLE).exclude(status=UserMission.DONE).exclude(status=UserMission.AVAILABLE)

        if not couple_missions.exists():
            un_cleared_mission_pks = []
            for couple_mission in couple_missions:
                un_cleared_mission_pks.append(couple_mission.mission.pk)
        else:
            return None

        return un_cleared_mission_pks

    def do_mission(self, pk):
        method_name = 'do_mission_%s' % str(pk)
        method_to_call = getattr(MissionHandler, method_name)
        return method_to_call.__call__(self, pk)

    def do_mission_1(self, pk):
        """
        사진 1개 업로드 하기 미션
        """
        mission = Mission.objects.get(pk=pk)
        couple_mission = UserMission.objects.get(
            mission=mission, couple=self.couple)
        started_datetime = couple_mission.started_datetime

        if Photo.objects.filter(created_at__gte=started_datetime).exists():
            couple_mission.status = 2
            couple_mission.finished_time = datetime.utcnow()
            couple_mission.save()

        return couple_mission
        mission = Mission.objects.get(pk=pk)
        couple_mission = UserMission.objects.get(
            mission=mission, couple=self.couple)
        return couple_mission

    def do_mission_2(self, pk):
        """
        편지 1개 업로드 하기 미션
        """
        mission = Mission.objects.get(pk=pk)
        couple_mission = UserMission.objects.get(
            mission=mission, couple=self.couple)
        started_datetime = couple_mission.started_datetime
        if Letter.objects.filter(created_at__gte=started_datetime).exists():
            couple_mission.status = 2
            couple_mission.finished_time = datetime.utcnow()
            couple_mission.save()  # couple_mission.save()

        return couple_mission


class OneTimeMissionHandler():

    def __init__(self, request_obj, mission_id):
        if not isinstance(request_obj.user, User):
            raise Exception('must pass User object')

        self.request_obj = request_obj
        self.user = self.request_obj.user
        self.couple = CoupleController.get_couple(self.user)

        self.mission = Mission.objects.get(id=mission_id)
        self.couple_mission, created = UserMission.objects.get_or_create(
            couple=self.couple, mission=self.mission)

    def has_cleared(self):
        return self.couple_mission.status

    def do_mission(self):
        method_name = 'do_mission_%s' % str(self.mission.pk)
        method_to_call = getattr(OneTimeMissionHandler, method_name)
        return method_to_call.__call__(self)

    def __validate_mission_1__(self, gender, birthdate, first_date):

        error_dic = {}

        if gender.upper() not in ['M', 'F']:
            error_dic['type'] = 'gender'
            error_dic['message'] = _(u'성별의 형식이 잘못 되었습니다.')
            return error_dic

        try:
            parser.parse(birthdate)
        except:
            error_dic['type'] = 'birthdate'
            error_dic['message'] = _(u'생년월일의 형식이 잘못 되었습니다.')
            return error_dic

        try:
            parser.parse(first_date)
        except:
            error_dic['type'] = 'first_date'
            error_dic['message'] = _(u'사귄날의 형식이 잘못 되었습니다.')
            return error_dic
        return None

    def do_mission_3(self):
        """
        튜토리얼 미션
        """

        try:
            first_name = self.request_obj.DATA['first_name']
            last_name = self.request_obj.DATA['last_name']
            gender = self.request_obj.DATA['gender']
            birthdate = self.request_obj.DATA['birthdate']
            first_date = self.request_obj.DATA['first_date']

            image = self.request_obj.FILES['image']
        except:
            return False

        error_dic = self.__validate_mission_1__(
            gender, birthdate, first_date)

        if error_dic:
            return False

        user = self.user
        userprofile = user.userprofile
        couple = self.couple

        user.first_name = first_name
        user.last_name = last_name
        userprofile.gender = gender
        userprofile.birthdate = parser.parse(birthdate).date()
        couple.first_date = parser.parse(first_date).date()
        userprofile.image = image

        user.save()
        userprofile.save()
        couple.save()

        self.couple_mission.status = UserMission.REWARDABLE
        self.couple_mission.save()

        return True
