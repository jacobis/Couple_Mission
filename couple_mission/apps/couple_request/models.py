from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Project Libs
from couple_mission.libs.common.model import TimeStampModel


class CoupleRequest(TimeStampModel):
    user = models.ForeignKey(User)
    request_sender = PhoneNumberField(help_text='E.g +41524204242')
    request_receiver = PhoneNumberField(help_text='E.g +41524204242')
    connected = models.BooleanField("Connected", default=False)

    class Meta:
        db_table = "couple_request"
