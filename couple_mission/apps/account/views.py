# Django
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, link, api_view
from rest_framework.parsers import JSONParser

# REST Framework Authentication & Permissions
from rest_framework.authtoken.models import Token
from rest_framework import permissions

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
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)

            return Response(
                {'success': True, 'message': _(u'Sign up success.')}, status=status.HTTP_201_CREATED,
                headers=headers)

        return Response({'success': False, 'message': _(u'%s') % serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def login(request):
    return Response('1234')
