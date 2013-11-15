from django.db import models

# Project
from couple_mission.apps.account.models import UaiUser
from couple_mission.apps.couple.models import Couple

# Project Utils
from couple_mission.libs.utils.storage import getfilesystem


class Contents(models.Model):
    user = models.ForeignKey(UaiUser)
    couple = models.ForeignKey(Couple)

    class Meta:
        abstract = True

class Comment(Contents):
    content = models.CharField("Content", max_length=200)

    class Meta:
        db_table = "contents_comment"

class PhotoAlbum(models.Model):
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "contents_photo_album"

class Photo(Contents):
    album = models.ForeignKey(PhotoAlbum)
    comment = models.ForeignKey(Comment)
    image = models.ImageField("Image", upload_to='photo/', storage=getfilesystem())
    description = models.TextField("Description", default="", blank=True, null=True)

    class Meta:
        db_table = "contents_photo"

class Letter(Contents):
    content = models.TextField("Content")
    reading = models.BooleanField("Reading", default=False)

    class Meta:
        db_table = "contents_letter"
