from django.contrib.auth.models import User


class CoupleController(object):

    @classmethod
    def get_couple(cls, user):
        if isinstance(user, User):
            couple_queryset = user.partner_a.all() | user.partner_b.all()
            couple = couple_queryset[0] if couple_queryset else None
            return couple
        else:
            raise Exception('Need token.')
