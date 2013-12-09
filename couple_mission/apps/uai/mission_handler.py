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

        first_name = self.DATA.get('first_name', None)
        last_name = self.DATA.get('last_name', None)
        gender = self.DATA.get('gender', None)
        birthdate = self.DATA.get('birthdate', None)
        first_date = self.DATA.get('first_date', None)

        image = self.FILES.get('image', None)

        error_dic = self.__validate__(
            first_name, last_name, gender, birthdate, first_date)

        if error_dic:
            error_type = error_dic['type']
            message = error_dic['message']
            return Response({'success': False, 'type': error_dic['type'], 'message': error_dic['message']}, status=status.HTTP_400_BAD_REQUEST)

        user = self.user
        print user
        userprofile = user.userprofile
        couple = CoupleController.get_couple(user)

        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        if gender is not None:
            userprofile.gender = gender

        if birthdate is not None:
            userprofile.birthdate = parser.parse(birthdate).date()

        if first_date is not None:
            couple.first_date = parser.parse(first_date).date()

        if image is not None:
            userprofile.image = image

        user.save()
        userprofile.save()
        couple.save()

        return Response({'success': True}, status=status.HTTP_200_OK)
        result = {}
        return result
