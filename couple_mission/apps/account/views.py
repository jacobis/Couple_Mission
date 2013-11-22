# Django
from django.contrib.auth.models import User

# REST Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, link

# Project
from couple_mission.apps.account.serializers import AccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Users list, create, retrieve, update, destroy
    """
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    @action(methods=['POST', 'DELETE'])
    def singup(self, request):
        pass