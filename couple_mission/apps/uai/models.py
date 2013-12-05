from django.db import models

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class MissionCategory(TimeStampModel):
    name = models.CharField("Name", max_length=100)

    class Meta:
        db_table = "uai_mission_category"

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

    class Meta:
        db_table = "uai_mission"

    def __unicode__(self):
        return self.title


class Badge(TimeStampModel):
    name = models.CharField("Name", max_length=100)
    description = models.TextField(
        "Description", default="", blank=True, null=True)
    image = models.ImageField(
        "Image", upload_to='badge/', storage=getfilesystem(), blank=True, null=True)

    class Meta:
        db_table = "uai_badge"

    def __unicode__(self):
        return self.name


class Title(TimeStampModel):
    name = models.CharField("Name", max_length=100)

    class Meta:
        db_table = "uai_title"

    def __unicode__(self):
        return self.name
