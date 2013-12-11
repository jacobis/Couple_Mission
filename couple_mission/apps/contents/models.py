from django.db import models
from django.contrib.auth.models import User

# Project
from couple_mission.apps.couple.models import Couple

# Project Libs
from couple_mission.libs.common.model import TimeStampModel
from couple_mission.libs.utils.storage import getfilesystem


class CommentManager(TimeStampModel):

    class Meta:
        db_table = "comment_manager"


class BaseContents(TimeStampModel):
    user = models.ForeignKey(User)
    couple = models.ForeignKey(Couple)
    comment_manager = models.OneToOneField(CommentManager)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if not self.pk:
            comment_manager = CommentManager.objects.create()
            self.comment_manager = comment_manager

        super(BaseContents, self).save(*args, **kwargs)


class Comment(TimeStampModel):
    comment_manager = models.ForeignKey(
        CommentManager, related_name='comments')
    user = models.ForeignKey(User, related_name='has_comments')
    content = models.CharField("Content", max_length=200)

    class Meta:
        db_table = "contents_comment"
        ordering = ['created_at']


class PhotoAlbum(TimeStampModel):
    couple = models.ForeignKey(Couple, related_name="photo_albums")
    title = models.CharField("Title", max_length=100)

    class Meta:
        db_table = "contents_photo_album"

    def __unicode__(self):
        return "(%s)%s" % (self.pk, self.title)


class Photo(BaseContents):
    album = models.ForeignKey(PhotoAlbum, default="", blank=True, null=True)
    image = models.ImageField(
        "Image", upload_to='photo/', storage=getfilesystem())
    description = models.TextField(
        "Description", default="", blank=True, null=True)

    class Meta:
        db_table = "contents_photo"
        ordering = ['-created_at']

    @property
    def image_url(self):
        return self.image.url if self.image else ''


class Letter(BaseContents):
    # Paper Type
    PLAIN = 0
    PAPER_TYPE_CHOICE = ((PLAIN, "Plain"),)

    receiver = models.ForeignKey(
        User, related_name='recieved', blank=True, null=True)
    content = models.TextField("Content")
    already_read = models.BooleanField("Already read", default=False)
    paper_type = models.IntegerField(
        "Paper type", choices=PAPER_TYPE_CHOICE, default=PLAIN)

    class Meta:
        db_table = "contents_letter"

    @property
    def gender(self):
        return self.user.userprofile.gender
