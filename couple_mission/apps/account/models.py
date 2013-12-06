from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class UserProfile(TimeStampModel):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, unique=True, primary_key=True)
    birthdate = models.DateField("Birth Date", null=True, blank=True)
    gender = models.CharField("Gender", max_length=1, null=True, blank=True)
    image = models.ImageField(
        "Image", upload_to='user_profile/', storage=getfilesystem(), null=True, blank=True)

    class Meta:
        db_table = "account_user_profile"

    def __unicode__(self):
        return self.user.username
