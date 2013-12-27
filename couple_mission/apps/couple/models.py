from django.db import models
from django.contrib.auth.models import User

# Project
from couple_mission.apps.uai.models import Badge, Title

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
        "Image", upload_to='couple/', storage=getfilesystem('usercontents'), null=True, blank=True)

    class Meta:
        unique_together = ("partner_a", "partner_b")
        db_table = "couple"

    def __unicode__(self):
        member = "%s, %s" % (self.partner_a.username, self.partner_b.username)
        return member

    @property
    def image_url(self):
        return self.image.url if self.image else ''


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
