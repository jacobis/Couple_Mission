from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin

 
class UaiUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    birthdate = models.DateField("Birth Date", null=True, blank=True)

    class Meta:
        db_table = "account_user_profile"

    def __unicode__(self):
        return self.user.username