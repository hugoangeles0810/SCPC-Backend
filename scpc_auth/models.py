import binascii
import os

from django.db import models as ext
from django.utils.translation import gettext_lazy as _

from scpc_core import models as core
from scpc_core.models import mixins

"""
Functions
"""
def generate_key():
  return binascii.hexlify(os.urandom(20)).decode()


"""
Classes
"""
class Token(mixins.ActiveMixin):
  key = ext.CharField(_("Key"), max_length=40, unique=True)
  user = ext.ForeignKey(core.User, related_name='auth_tokens')

  class Meta:
    verbose_name = _("Token")
    verbose_name_plural = _("Tokens")

  def __str__(self):
    return self.key

  def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    if not self.key:
        self.key = generate_key()
    super().save(force_insert, force_update, using, update_fields)