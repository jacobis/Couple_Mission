from django.db import models
from django.contrib.auth.models import User

# Project Libs
from couple_mission.libs.common.model import TimeStampModel


class UserProfile(TimeStampModel):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    birthdate = models.DateField("Birth Date", null=True, blank=True)

    class Meta:
        db_table = "account_user_profile"

    def __unicode__(self):
        return self.user.username
