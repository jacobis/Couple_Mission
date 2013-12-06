from rest_framework import serializers

from couple_mission.apps.couple_request.models import CoupleRequest


class CoupleRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoupleRequest
