# Django
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

# REST Framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import action, link, api_view
from rest_framework.parsers import JSONParser

# REST Framework Authentication & Permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Project
from couple_mission.apps.account.models import UserProfile
from couple_mission.apps.account.serializers import UserSerializer
from couple_mission.apps.account.serializers import UserProfileSerializer
from couple_mission.apps.account.serializers import AuthTokenSerializer
from couple_mission.apps.couple.controller import CoupleController

from django.contrib.auth import authenticate


class UserViewSet(viewsets.ModelViewSet):

    """
    Users list, create, retrieve, update, destroy
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            token = Token.objects.get(user=self.object)

            return Response(
                {'success': True, 'message': _(u'Sign up success.'), 'token': token.key}, status=status.HTTP_201_CREATED,
                headers=headers)

        return Response({'success': False, 'message': _(u'%s') % serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
            UserProfile.objects.create(user=instance)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    model = Token

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.DATA)

        if serializer.is_valid():
            token, created = Token.objects.get_or_create(
                user=serializer.object['user'])
            return Response({'success': True, 'token': token.key})
        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Me(APIView):

    def get(self, request):
        couple = CoupleController.get_couple(request.user)
        print couple
        couple_id = couple.pk if couple else 0
        user_id = request.user.pk

        return Response({'couple_id': couple_id, 'user_id': user_id})


obtain_auth_token = ObtainAuthToken.as_view()
me = Me.as_view()
