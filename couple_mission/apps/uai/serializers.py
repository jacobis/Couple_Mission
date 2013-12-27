from couple_mission.apps.uai.models import Badge, Title

from rest_framework import serializers


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
