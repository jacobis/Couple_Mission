from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Django REST Framework
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# Projects
from couple_mission.apps.account.views import UserViewSet, UserProfileViewSet
from couple_mission.apps.couple_request.views import CoupleRequestViewSet
from couple_mission.apps.couple.views import CoupleViewSet, CoupleMissionViewSet
from couple_mission.apps.contents.views import CommentViewSet, PhotoAlbumViewSet, PhotoViewSet, LetterViewSet
from couple_mission.apps.uai.views import BadgeViewSet, TitleViewSet
from couple_mission.apps.headquarter.views import NoticeViewSet


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
                        url(r'^$',
                            'views.main_index'),
                        )

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'couple_requests', CoupleRequestViewSet)
router.register(r'couples', CoupleViewSet)
router.register(r'couple_missions', CoupleMissionViewSet)
router.register(r'badges', BadgeViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'photo_albums', PhotoAlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'letters', LetterViewSet)
router.register(r'notices', NoticeViewSet)
# urlpatterns += router.urls

urlpatterns += patterns('',
                        url(r'^api/v1/', include(router.urls)),
                        )
