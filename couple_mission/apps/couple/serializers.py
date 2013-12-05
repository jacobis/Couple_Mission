from django.contrib.auth.models import User
from couple_mission.apps.couple.models import Couple

from rest_framework import serializers


class CoupleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Couple

# class CoupleMissionSerializer(serializers.ModelSerializer):
