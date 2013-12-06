# -*- coding: utf-8 -*-

# Django
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, link

# RESE Framework Authentication & Permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Project
from couple_mission.apps.couple.models import Couple
from couple_mission.apps.couple_request.models import CoupleRequest
from couple_mission.apps.couple_request.serializers import CoupleRequestSerializer

# Other
from phonenumber_field.phonenumber import to_python


class CoupleRequestViewSet(viewsets.ModelViewSet):
    qeuryset = CoupleRequest.objects.all()
    serializer_class = CoupleRequestSerializer
    model = CoupleRequest
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)
        user = request.user
        message = _(u"이미 커플인 회원입니다.")

        if not Couple.objects.filter(Q(partner_a=user) | Q(partner_b=user)):
            request_sender = request.DATA['request_sender']
            request_receiver = request.DATA['request_receiver']
            result, message = self.validate_couple_request(
                request_sender, request_receiver)
            if result:
                requests = CoupleRequest.objects.filter(
                    request_receiver=request_sender, connected=False)

                if requests:
                    for r in requests:
                        if unicode(r.request_sender) == request_receiver:
                            couple, created = Couple.objects.get_or_create(
                                partner_a=user, partner_b=r.user)
                            r.connected = True
                            r.save()

                            return Response({'success': True, 'message': _(u'Congratulation! Couple Connencted.')}, status=status.HTTP_201_CREATED)
                else:
                    CoupleRequest.objects.get_or_create(
                        user=user, request_sender=request_sender, request_receiver=request_receiver)

                    return Response({'success': True, 'message': _(u'Waiting for response from partner.')}, status=status.HTTP_201_CREATED)

        return Response({'success': False, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

    def validate_couple_request(self, request_sender, request_receiver):
        request_sender = to_python(request_sender)
        request_receiver = to_python(request_receiver)

        if request_sender is None or request_receiver is None:
            return False, _(u"전화번호는 필수값 입니다.")

        if not request_sender.is_valid() and not request_receiver.is_valid():
            return False, _(u"잘못된 형식의 번호입니다.")

        if request_sender == request_receiver:
            return False, _(u"나의 번호와 상대방 번호는 같을 수 없습니다.")

        return True, None
