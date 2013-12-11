# -*- coding: utf-8 -*-

from dateutil import parser

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from couple_mission.apps.uai.models import Mission
from couple_mission.apps.couple.models import CoupleMission
from couple_mission.apps.couple.controller import CoupleController


class MissionHandler():

    def __init__(self, request_obj, mission_id):
        if not isinstance(request_obj.user, User):
            raise Exception('must pass User object')

        self.request_obj = request_obj
        self.user = self.request_obj.user
        self.couple = CoupleController.get_couple(self.user)

        self.mission = Mission.objects.get(id=mission_id)
        self.couple_mission, created = CoupleMission.objects.get_or_create(
            couple=self.couple, mission=self.mission)

    def has_cleared(self):
        return self.couple_mission.status

    def do_mission(self):
        method_name = 'do_mission_%s' % str(self.mission.pk)
        method_to_call = getattr(MissionHandler, method_name)
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

    def do_mission_1(self):

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

        self.couple_mission.status = True
        self.couple_mission.save()

        return True
