from django.contrib import admin
from django.conf.urls import patterns, include, url

# Django REST Framework
from rest_framework import routers

# Projects
from couple_mission.apps.account.views import UserViewSet
from couple_mission.apps.couple.views import CoupleViewSet
from couple_mission.apps.contents.views import CommentViewSet, PhotoAlbumViewSet, PhotoViewSet, LetterViewSet


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'couples', CoupleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'photo_albums', PhotoAlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'letters', LetterViewSet)
urlpatterns += router.urls