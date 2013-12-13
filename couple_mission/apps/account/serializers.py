# -*- coding: utf-8 -*-

import re

from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from couple_mission.apps.account.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image_url')

    class Meta:
        model = UserProfile
        fields = ('user', 'birthdate', 'gender', 'image')
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def validate(self, attrs):
        email = attrs['email']

        if not email:
            raise serializers.ValidationError(_(u'이메일을 입력해주세요.'))

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(_(u'이미 등록된 이메일 주소입니다.'))

        return email

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
            password = make_password(password)
            first_name = attrs.get('first_name', '')
            last_name = attrs.get('last_name', '')
            username = email[:email.index('@')]

            return User(username=username, email=email, password=password, first_name=first_name, last_name=last_name)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        username = User.objects.get(email=email)

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError(
                        _(u'해당 사용자는 사용불가 상태입니다.'))
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError(
                    _(u'이메일 또는 패스워드가 잘못되었습니다.'))
        else:
            raise serializers.ValidationError(
                _(u'이메일 또는 패스워드를 다시 한 번 확인해주세요.'))
