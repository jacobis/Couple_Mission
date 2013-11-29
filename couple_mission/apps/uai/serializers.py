from couple_mission.apps.uai.models import MissionCategory, Mission, Badge, Title

from rest_framework import serializers


class MissionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MissionCategory


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
