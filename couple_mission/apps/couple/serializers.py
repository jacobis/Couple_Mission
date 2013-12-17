from datetime import datetime, date

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
    dday = serializers.SerializerMethodField('get_dday')

    class Meta:
        model = CoupleDday

    def get_dday(self, obj):
        dday = obj.date - datetime.utcnow().date()
        dday = str((dday.days) * -1)
        return dday
