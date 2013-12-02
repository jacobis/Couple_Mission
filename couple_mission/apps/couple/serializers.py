from django.contrib.auth.models import User
from couple_mission.apps.couple.models import Couple

from rest_framework import serializers


class CoupleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Couple

    # def validate(self, attrs):

    #     if attrs['male'] == attrs['female']:
    #         raise serializers.NestedValidationError(
    #             "Couple is not consist of same user")
    #     else:
    #         if Couple.objects.filter(male=attrs['male']).exists() or Couple.objects.filter(female=attrs['male']).exists():
    #             raise serializers.ValidationError(
    #                 "%s is already couple" % attrs['male'])
    #         if Couple.objects.filter(male=attrs['female']).exists() or Couple.objects.filter(female=attrs['female']).exists():
    #             raise serializers.ValidationError(
    #                 "%s is already couple" % attrs['female'])
    #     return attrs
