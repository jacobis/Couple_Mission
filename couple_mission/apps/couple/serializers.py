from django.contrib.auth.models import User
from couple_mission.apps.couple.models import Couple

from rest_framework import serializers


class CoupleSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image_url')

    class Meta:
        model = Couple
        fields = ('partner_a', 'partner_b', 'first_date', 'image')
