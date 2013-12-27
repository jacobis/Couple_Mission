from rest_framework import serializers

from couple_mission.apps.mission.models import UserMission


class UserMissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMission
