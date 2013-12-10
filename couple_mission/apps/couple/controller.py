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

    @classmethod
    def get_partner(cls, couple, user):
        if couple.partner_a == user:
            return couple.partner_b
        else:
            return couple.partner_a
