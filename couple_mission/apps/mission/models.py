from django.db import models
from django.contrib.auth.models import User

from couple_mission.apps.couple.models import Couple

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class ActiveMissionManager(models.Manager):

    def get_query_set(self):
        return super(ActiveMissionManager, self).get_query_set().filter(is_active=True)


class MissionCategory(TimeStampModel):
    identity = models.CharField("Identify", max_length=10)
    name = models.CharField("Name", max_length=100)

    class Meta:
        db_table = "mission_mission_category"

    def __unicode__(self):
        return self.name


class Mission(TimeStampModel):
    category = models.ForeignKey(MissionCategory)
    title = models.CharField("Title", max_length=200)
    description = models.TextField(
        "Description", default="", blank=True, null=True)
    image = models.ImageField(
        "Image", upload_to='mission/', storage=getfilesystem(), blank=True, null=True)
    point = models.IntegerField("Point", default="0")
    is_active = models.BooleanField("Is Active", default=False)

    objects = models.Manager()
    active = ActiveMissionManager()

    class Meta:
        db_table = "mission_mission"
        ordering = ['created_at']

    def __unicode__(self):
        return self.title


class UserMission(TimeStampModel):
    # Couple Mission Status
    AVAILABLE = 0
    DOING = 1
    REWARDABLE = 2
    DONE = 3

    USER_MISSION_STATUS_CHOICE = (
        (AVAILABLE, 0), (DOING, 1), (REWARDABLE, 2), (DONE, 3))

    user = models.ForeignKey(User)
    couple = models.ForeignKey(Couple)
    mission = models.ForeignKey(Mission)
    status = models.IntegerField(
        "Status", choices=USER_MISSION_STATUS_CHOICE, default=AVAILABLE)
    started_datetime = models.DateTimeField(blank=True, null=True)
    claered_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "user_mission"
        ordering = ['-updated_at']
