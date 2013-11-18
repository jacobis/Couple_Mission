from rest_framework import serializers
from couple_mission.apps.account.models import UaiUser

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UaiUser
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active')