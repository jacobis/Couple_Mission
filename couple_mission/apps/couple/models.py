from django.db import models

# Project
from couple_mission.apps.account.models import User
from couple_mission.apps.uai.models import Mission, Badge, Title

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class Couple(TimeStampModel):
    partner_a = models.ForeignKey(
        User, related_name='partner_a', null=True, blank=True)
    partner_b = models.ForeignKey(
        User, related_name='partner_b', null=True, blank=True)
    first_date = models.DateField("Date", null=True, blank=True)
    image = models.ImageField(
        "Image", upload_to='couple/', storage=getfilesystem(), null=True, blank=True)

    class Meta:
        unique_together = ("partner_a", "partner_b")
        db_table = "couple"

    def __unicode__(self):
        member = "%s, %s" % (self.partner_a.username, self.partner_b.username)
        return member


class CoupleMission(TimeStampModel):
    couple = models.ForeignKey(Couple)
    mission = models.ForeignKey(Mission)
    status = models.BooleanField("Status", default=False)

    class Meta:
        db_table = "couple_mission"


class CoupleBadge(TimeStampModel):
    couple = models.ForeignKey(Couple)
    badge = models.ForeignKey(Badge)
    status = models.BooleanField("Status", default=False)

    class Meta:
        db_table = "couple_badge"


class CoupleTitle(TimeStampModel):
    couple = models.ForeignKey(Couple)
    title = models.ForeignKey(Title)
    status = models.BooleanField("Status", default=False)

    class Meta:
        db_table = "couple_title"


class CoupleDday(TimeStampModel):
    couple = models.ForeignKey(Couple)
    date = models.DateField("Date")
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "couple_d-day"
