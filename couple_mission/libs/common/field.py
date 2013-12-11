from django.utils import timezone

from rest_framework import serializers


class LocalizedDateTimeField(serializers.Field):

    def to_native(self, data):

        tz = timezone.get_current_timezone()

        return tz.normalize(data)
