# -*- coding: utf-8 -*-

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
from couple_mission.apps.couple.serializers import CoupleSerializer
from couple_mission.apps.uai.views import Mission
from couple_mission.apps.contents.models import PhotoAlbum

# Project Libs
from couple_mission.libs.common.string import sanitize


class CoupleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer

    @receiver(post_save, sender=Couple)
    def initialize_couple(sender, instance=None, created=False, **kwargs):
        if created:
            PhotoAlbum.objects.create(couple=instance, title=_(u"기본앨범"))

# class CoupleMissionViewSet(viewsets.ModelViewSet):
#     queryset = CoupleMission.objects.all()
#     serializer_class =


# class CoupleMisson():

#     def check_mission(self):
#         Mission.letter_mission()
