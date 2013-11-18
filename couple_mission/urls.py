from django.contrib import admin
from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = patterns('couple_mission.apps.account.views',
    url(r'users/$', 'user_list'),
    url(r'user/(?P<pk>[0-9]+)/$', 'user_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)