# Django
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, link

# REST Framework Auth
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication


# Project
from couple_mission.apps.account.models import UserProfile
from couple_mission.apps.account.serializers import UserSerializer
from couple_mission.apps.account.serializers import UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):

    """
    Users list, create, retrieve, update, destroy
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
