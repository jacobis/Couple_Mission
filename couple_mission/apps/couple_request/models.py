from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from couple_mission.apps.account.models import User


class CoupleRequest(models.Model):
    user = models.ForeignKey(User)
    request_sender = PhoneNumberField(help_text='E.g +41524204242')
    request_receiver = PhoneNumberField(help_text='E.g +41524204242')
    connected = models.BooleanField("Connected", default=False)

    class Meta:
        db_table = "couple_request"
