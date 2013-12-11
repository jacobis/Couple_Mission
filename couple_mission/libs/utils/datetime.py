from django.utils import timezone


def normalize(data):

    tz = timezone.get_current_timezone()

    return tz.normalize(data)
