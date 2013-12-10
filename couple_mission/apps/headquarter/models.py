# Django
from django.db import models

# Project Libs
from couple_mission.libs.common.model import TimeStampModel


class Notice(TimeStampModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "headquarter_notice"

    def __unicode__(self):
        return self.title
