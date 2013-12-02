import re

from django.contrib.auth.models import User
from django.core.validators import validate_email

from rest_framework import serializers

from couple_mission.apps.account.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('birthdate',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.email = attrs.get('email', instance.email)
            instance.password = attrs.get('password', instance.password)
            instance.first_name = attrs.get('first_name', instance.first_name)
            instance.last_name = attrs.get('last_name', instance.last_name)
            instance.username = attrs.get(
                'username', instance.email[:instance.email.index('@')])
            return instance

        else:
            email = attrs.get('email')
            password = attrs.get('password')
            first_name = attrs.get('first_name', None)
            last_name = attrs.get('last_name', None)
            username = email[:email.index('@')]

        return User(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

    def validate_email(self, attrs, source):
        value = attrs[source]
        try:
            if self.object.email:
                raise serializers.ValidationError("Email change")
                # require editing
        except:
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Email already exists")
            else:
                return attrs
