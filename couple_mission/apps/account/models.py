from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin

 
class UaiUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

class UserProfile(models.Model):
    user = models.OneToOneField(UaiUser, unique=True, primary_key=True)
    birthdate = models.DateField("Birth Date", null=True, blank=True)

    class Meta:
        db_table = "account_user_profile"

    def __unicode__(self):
        return self.user.username