# Django
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.couple.models import Couple
from couple_mission.apps.couple_request.models import CoupleRequest
from couple_mission.apps.couple_request.serializers import CoupleRequestSerializer


class CoupleRequestViewSet(viewsets.ModelViewSet):
    qeuryset = CoupleRequest.objects.all()
    serializer_class = CoupleRequestSerializer
    model = CoupleRequest

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)
        user_id = request.DATA['user']
        user = User.objects.get(id=user_id)

        if not Couple.objects.filter(Q(male=user)|Q(female=user)):
            if serializer.is_valid():
                request_sender = request.DATA['request_sender']
                request_receiver = request.DATA['request_receiver']
                requests = CoupleRequest.objects.filter(request_receiver=request_sender, connected=False)

                if requests:
                    for r in requests:
                        if unicode(r.request_sender) == request_receiver:
                            couple, created = Couple.objects.get_or_create(male=user, female=r.user)
                            r.connected = True
                            r.save()
                            
                            return Response({'status': 'Congratulation! Couple Connencted.'})
                else:
                    CoupleRequest.objects.get_or_create(user=user, request_sender=request_sender, request_receiver=request_receiver)
                    return Response({'status': 'Wait a sec'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)