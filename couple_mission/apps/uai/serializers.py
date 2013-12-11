from couple_mission.apps.uai.models import MissionCategory, Badge, Title

from rest_framework import serializers


class MissionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MissionCategory


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
