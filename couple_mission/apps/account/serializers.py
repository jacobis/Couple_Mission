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

    def validate_email(self, attrs, source):
        value = attrs[source]

        try:
            validate_email(value)
        except:
            raise serializers.ValidationError("Email is not normal")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is exists")

        return attrs

    def restore_object(self, attrs, instance=None):
        if instance:
            pass
        else:
            email = attrs.get('email')
            password = attrs.get('password')
            first_name = attrs.get('first_name', None)
            last_name = attrs.get('last_name', None)
            username = email[:email.index('@')]

        return User(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
