import pygeoip
from pygeoip import GeoIP

from django.conf import settings
from django.utils import timezone


class TimezoneMiddleware(object):

    '''
    classdocs
    '''

    def process_request(self, request):
        tz = request.session.get('django_timezone')

        time_zone = tz if tz else self.get_time_zone_by_ip(request)

        if not time_zone:
            time_zone = settings.TIME_ZONE

        timezone.activate(time_zone)

    def get_time_zone_by_ip(self, request):
        '''
        http://packages.python.org/pygeoip/
        '''

        gi = GeoIP(settings.GEOIP_PATH + settings.GEOIP_CITY, pygeoip.STANDARD)
        client_ip = request.get_host().split(':')[0]

        try:
            time_zone = gi.time_zone_by_addr(client_ip)
        except:
            return None
        else:
            if not time_zone:
                client_ip = request.META.get('REMOTE_ADDR')
                time_zone = gi.time_zone_by_addr(client_ip)

        return time_zone
