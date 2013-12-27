from django.db import models

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class Badge(TimeStampModel):
    name = models.CharField("Name", max_length=100)
    description = models.TextField(
        "Description", default="", blank=True, null=True)
    image = models.ImageField(
        "Image", upload_to='badge/', storage=getfilesystem('admincontents'), blank=True, null=True)

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
