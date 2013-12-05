from django.contrib import admin
from django.conf.urls import patterns, include, url

# Django REST Framework
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# Projects
from couple_mission.apps.account.views import UserViewSet
from couple_mission.apps.couple_request.views import CoupleRequestViewSet
from couple_mission.apps.couple.views import CoupleViewSet
from couple_mission.apps.contents.views import CommentViewSet, PhotoAlbumViewSet, PhotoViewSet, LetterViewSet
from couple_mission.apps.uai.views import MissionCategoryViewSet, MissionViewSet, BadgeViewSet, TitleViewSet


# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
                       # Admin panel and documentation:
                       url(r'^admin/doc/', include(
                           'django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += patterns('',
                        url(r'^login/', 'couple_mission.apps.account.views.login'),
                        )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'couple_requests', CoupleRequestViewSet)
router.register(r'couples', CoupleViewSet)
router.register(r'mission_categories', MissionCategoryViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'badges', BadgeViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'photo_albums', PhotoAlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'letters', LetterViewSet)
urlpatterns += router.urls
