# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from couple_mission.apps.uai.models import Mission
from couple_mission.apps.couple.controller import CoupleController


class MissionHandler():

    def __init__(self, request_obj, mission_id):
        if not isinstance(request_obj.user, User):
            raise Exception('must pass User object')

        self.request_obj = request_obj
        self.user = self.request_obj.user
        self.couple = CoupleController.get_couple(self.user)

        mission = Mission.objects.get(id=mission_id)
        self.couple_mission = CoupleMission.get_or_create(
            couple=self.couple, mission=mission)

    def has_cleared(self):
        return self.couple_mission.status

    def do_mission(self):
        method_name = 'do_mission_%s' % str(self.mission.pk)
        method_to_call = getattr(MissionHandler, method_name)
        return method_to_call.__call__(self)

    # def __validate__(self, first_name, last_name, gender, birthdate, first_date):
    #     name_reg = re.compile(r"^[a-zA-Z0-9]{0,30}$")
    #     error_dic = {}
    #     if first_name is not None:
    #         if not name_reg.match(first_name):
    #             error_dic['type'] = 'first_name'
    #             error_dic['message'] = _(u'이름의 형식이 잘못 되었습니다.')
    #             return error_dic
    #     if last_name is not None:
    #         if not name_reg.match(last_name):
    #             error_dic['type'] = 'last_name'
    #             error_dic['message'] = _(u'성의 형식이 잘못 되었습니다.')
    #             return error_dic
    #     if gender is not None:
    #         if gender.upper() not in ['M', 'F']:
    #             error_dic['type'] = 'gender'
    #             error_dic['message'] = _(u'성별의 형식이 잘못 되었습니다.')
    #             return error_dic
    #     if birthdate is not None:
    #         try:
    #             parser.parse(birthdate)
    #         except:
    #             error_dic['type'] = 'birthdate'
    #             error_dic['message'] = _(u'생년월일의 형식이 잘못 되었습니다.')
    #             return error_dic
    #     if first_date is not None:
    #         try:
    #             parser.parse(first_date)
    #         except:
    #             error_dic['type'] = 'first_date'
    #             error_dic['message'] = _(u'사귄날의 형식이 잘못 되었습니다.')
    #             return error_dic
    #     return None

    def do_mission_1(self):
        result = {}
        return result
