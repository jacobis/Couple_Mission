# -*- coding: utf-8 -*-

# Django
from django.db.models import Q
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

# RESE Framework Authentication & Permissions
from rest_framework.permissions import IsAuthenticated

# Project
from couple_mission.apps.couple.models import Couple
from couple_mission.apps.couple_request.models import CoupleRequest
from couple_mission.apps.couple_request.serializers import CoupleRequestSerializer

# Project Libs
from couple_mission.libs.common.string import sanitize

# Other
from phonenumber_field.phonenumber import to_python


class CoupleRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    qeuryset = CoupleRequest.objects.all()
    serializer_class = CoupleRequestSerializer
    model = CoupleRequest
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)
        self.user = request.user

        request_sender = request.DATA['request_sender']
        request_receiver = request.DATA['request_receiver']
        result, message = self.validate_couple_request(
            request_sender, request_receiver)
        if result:
            requests = CoupleRequest.objects.filter(
                request_receiver=request_sender, connected=False).exclude(user=self.user)

            if requests:
                message = _(u'축하합니다. 커플이 되었습니다.')
                success_status_code = status.HTTP_200_OK
                for request in requests:
                    if unicode(request.request_sender) == request_receiver:
                        couple, created = Couple.objects.get_or_create(
                            partner_a=self.user, partner_b=request.user)
                        request.connected = True
                        request.save()

            else:
                message = _(u'상대방의 커플 요청을 기다리고 있습니다.')
                success_status_code = status.HTTP_201_CREATED
                couple_request, created = CoupleRequest.objects.get_or_create(
                    user=self.user)
                couple_request.request_sender = request_sender
                couple_request.request_receiver = request_receiver
                couple_request.save()

            return Response({'success': True, 'message': message}, status=success_status_code)

        return Response({'success': False, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

    def validate_couple_request(self, request_sender, request_receiver):
        request_sender = to_python(request_sender)
        request_receiver = to_python(request_receiver)
        user = self.user

        if Couple.objects.filter(Q(partner_a=user) | Q(partner_b=user)):
            return False, _(u"이미 커플로 등록된 이메일입니다.")

        if request_sender is None or request_receiver is None:
            return False, _(u"전화번호를 입력해주세요.")

        if not request_sender.is_valid() and not request_receiver.is_valid():
            return False, _(u"전화번호를 다시 한 번 확인해주세요.")

        if request_sender == request_receiver:
            return False, _(u"전화번호를 다시 한 번 확인해주세요.")

        return True, None
