from django.contrib import admin
from django.conf.urls import patterns, include, url

# Django REST Framework
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# Projects
from couple_mission.apps.account.views import UserViewSet, UserProfileViewSet
from couple_mission.apps.couple_request.views import CoupleRequestViewSet
from couple_mission.apps.couple.views import CoupleViewSet
from couple_mission.apps.contents.views import CommentViewSet, PhotoAlbumViewSet, PhotoViewSet, LetterViewSet
from couple_mission.apps.uai.views import MissionCategoryViewSet, MissionView, BadgeViewSet, TitleViewSet


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

urlpatterns += patterns('couple_mission.apps.account',
                        url(r'^api/v1/login$', 'views.obtain_auth_token'),
                        url(r'^api/v1/me$', 'views.me'),
                        )

urlpatterns += patterns('couple_mission.apps.uai',
                        url(r'^api/v1/mission/(?P<mission_id>\w+)$',
                            'views.mission_detail_view', name='mission_detail'),
                        )

urlpatterns += patterns('couple_mission.apps.uai',
                        url(r'^$',
                            'views.main_index'),
                        )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'couple_requests', CoupleRequestViewSet)
router.register(r'couples', CoupleViewSet)
router.register(r'mission_categories', MissionCategoryViewSet)
# router.register(r'missions', MissionView)
router.register(r'badges', BadgeViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'photo_albums', PhotoAlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'letters', LetterViewSet)
# urlpatterns += router.urls

urlpatterns += patterns('',
                        url(r'^api/v1/', include(router.urls)),
                        )
