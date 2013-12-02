from rest_framework import serializers

from couple_mission.apps.couple_request.models import CoupleRequest


class CoupleRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoupleRequest

    def validate(self, attrs):
        if attrs['request_sender'] == attrs['request_receiver']:
            raise serializers.ValidationError(
                "Request sender is diffrent from request receiver")
        return attrs
