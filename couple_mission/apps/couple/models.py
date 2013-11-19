from django.db import models

# Project
from couple_mission.apps.account.models import User
from couple_mission.apps.uai.models import Mission, Badge, Title


class Couple(models.Model):
    male = models.ForeignKey(User, related_name='male_from', null=True, blank=True)
    female = models.ForeignKey(User, related_name='female_from', null=True, blank=True)

    class Meta:
        unique_together = ("male", "female")
        db_table = "couple"

    def __unicode__(self):
        member = "%s, %s" % (self.male.username, self.female.username)
        return member

class CoupleMission(models.Model):
    couple = models.ForeignKey(Couple)
    mission = models.ForeignKey(Mission)
    status = models.BooleanField("Status", default=False)

    class Meta:
        db_table = "couple_mission"

class CoupleBadge(models.Model):
    couple = models.ForeignKey(Couple)
    badge = models.ForeignKey(Badge)
    status = models.BooleanField("Status", default=False)

    class Meta:
        db_table = "couple_badge"

class CoupleTitle(models.Model):
    couple = models.ForeignKey(Couple)
    title = models.ForeignKey(Title)
    status = models.BooleanField("Status", default=False)

    class Meta:
        db_table = "couple_title"

class CoupleDday(models.Model):
    couple = models.ForeignKey(Couple)
    date = models.DateField("Date")
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "couple_d-day"