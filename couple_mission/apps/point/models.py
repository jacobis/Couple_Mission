from django.db import models
from django.contrib.auth.models import User

# Project
from couple_mission.apps.couple.models import Couple, CoupleMission


class Point(models.Model):
    user = models.ForeignKey(User)
    couple = models.ForeignKey(Couple)
    couple_mission = models.ForeignKey(CoupleMission)
    point = models.IntegerField("Point", default="0")

    class Meta:
        db_table = "point"

    def __unicode__(self):
        return self.point