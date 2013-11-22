from django.contrib import admin
from django.conf.urls import patterns, include, url

# Django REST Framework
from rest_framework import routers

# Projects
from couple_mission.apps.account import views


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
router.register(r'users', views.UserViewSet)
# router.register(r'accounts', AccountViewSet)
urlpatterns += router.urls