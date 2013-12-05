from django.db import models
from django.contrib.auth.models import User

# Project
from couple_mission.apps.couple.models import Couple

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class Contents(TimeStampModel):
    user = models.ForeignKey(User)
    couple = models.ForeignKey(Couple)

    class Meta:
        abstract = True


class Comment(Contents):
    content = models.CharField("Content", max_length=200)

    class Meta:
        db_table = "contents_comment"


class PhotoAlbum(Contents):
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "contents_photo_album"


class Photo(Contents):
    album = models.ForeignKey(PhotoAlbum, default="", blank=True, null=True)
    comment = models.ForeignKey(Comment, default="", blank=True, null=True)
    image = models.ImageField(
        "Image", upload_to='photo/', storage=getfilesystem())
    description = models.TextField(
        "Description", default="", blank=True, null=True)

    class Meta:
        db_table = "contents_photo"


class Letter(Contents):
    content = models.TextField("Content")
    reading = models.BooleanField("Reading", default=False)

    class Meta:
        db_table = "contents_letter"
