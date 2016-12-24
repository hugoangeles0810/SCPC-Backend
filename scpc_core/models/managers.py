from django.contrib.auth.models import UserManager as DjangoUserManager
from django.utils import timezone

"""
Functions
"""
def get_now():
  return timezone.now()


"""
Classes
"""
class UserManager(DjangoUserManager):

  def _create_user(self, username, email, password, **extra_fields):
    user = super(UserManager, self)._create_user(username, email, password, **extra_fields)
    user.save()
    return user