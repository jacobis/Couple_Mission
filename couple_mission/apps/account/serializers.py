from rest_framework import serializers

from couple_mission.apps.account.models import UaiUser


class AccountSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    birthdate = serializers.DateField(required=False)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.first_name = attrs.get('first_name', instance.first_name)
            instance.last_name = attrs.get('last_name', instance.last_name)
            return instance

        return UaiUser(**attrs)