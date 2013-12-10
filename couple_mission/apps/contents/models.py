from django.db import models
from django.contrib.auth.models import User

# Project
from couple_mission.apps.couple.models import Couple

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class BaseContents(TimeStampModel):
    user = models.ForeignKey(User)
    couple = models.ForeignKey(Couple)
    comment_manager = models.OneToOneField(CommentManager)

    class Meta:
        abstract = True


class CommentManager(TimeStampModel):

    class Meta:
        db_table = "comment_manager"


class Comment(TimeStampModel):
    comment_manager = models.ForeignKey(
        CommentManager, related_name='comments')
    user = models.ForeignKey(User, related_name='has_comments')
    content = models.CharField("Content", max_length=200)

    class Meta:
        db_table = "contents_comment"


class PhotoAlbum(TimeStampModel):
    couple = models.ForeignKey(Couple, related_name="photo_albums")
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "contents_photo_album"

    def __unicode__(self):
        return "(%s)%s" % (self.pk, self.title)


class Photo(BaseContents):
    album = models.ForeignKey(PhotoAlbum, default="", blank=True, null=True)
    comment = models.ForeignKey(Comment, default="", blank=True, null=True)
    image = models.ImageField(
        "Image", upload_to='photo/', storage=getfilesystem())
    description = models.TextField(
        "Description", default="", blank=True, null=True)

    class Meta:
        db_table = "contents_photo"
        ordering = ['-created_at']


class Letter(BaseContents):
    content = models.TextField("Content")
    reading = models.BooleanField("Reading", default=False)

    class Meta:
        db_table = "contents_letter"
