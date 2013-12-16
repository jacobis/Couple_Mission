from django.contrib.auth.models import User
from couple_mission.apps.couple.models import Couple, CoupleMission, CoupleDday

from rest_framework import serializers


class CoupleSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image_url')

    class Meta:
        model = Couple
        fields = ('partner_a', 'partner_b', 'first_date', 'image')


class CoupleMissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoupleMission


class CoupleDdaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CoupleDday
