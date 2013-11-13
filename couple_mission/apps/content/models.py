from django.db import models
from django.contrib.auth.models import User

# Project
from couple_mission.apps.couple.models import Couple

# Project Utils
from couple_mission.libs.utils.storage import getfilesystem


class Content(models.Model):
    user = models.ForeignKey(User)
    couple = models.ForeignKey(Couple)

    class Meta:
        abstract = True

class Comment(Contents):
    content = models.CharField("Content", max_length=200)

    class Meta:
        db_table = "content_comment"

class PhotoAlbum(models.Model):
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "content_photo_album"

class Photo(Content):
    album = models.ForeignKey(PhotoAlbum)
    comment = models.ForeignKey(Comment)
    image = models.ImageField("Image", upload_to='photo/', storage=getfilesystem())
    description = models.TextField("Description", default="", blank=True, null=True)

    class Meta:
        db_table = "content_photo"

class Letter(Content):
    content = models.TextField("Content")
    reading = models.BooleanField("Reading", default=False)

    class Meta:
        db_table = "content_letter"
