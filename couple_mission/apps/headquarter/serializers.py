from rest_framework import serializers

from couple_mission.apps.headquarter.models import Notice


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
