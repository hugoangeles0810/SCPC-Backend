from django.db import models as ext
from django.utils.translation import gettext_lazy as _

from scpc_core.models.managers import get_now
from scpc.utils import setallattr


"""
Functions
"""
def deactivate(obj, deactivated_at=None):
  if not obj.active or obj.fixed:
      return
  if not deactivated_at:
      from scpc_core.models.managers import get_now
      deactivated_at = get_now()
  setallattr(obj, active=False, deactivated_at=deactivated_at)
  obj.save()

def activate(obj, activated_at=None):
  if obj.active or obj.fixed:
      return
  if not activated_at:
      from scpc_core.models.managers import get_now
      activated_at = get_now()
  setallattr(obj, active=True, activated_at=activated_at)
  obj.save()


"""
Classes
"""
class ActiveMixin(ext.Model):
  active = ext.BooleanField(_("active"), default=True)
  deactivated_at = ext.DateTimeField(_("deactivated at"), null=True, blank=True)
  activated_at = ext.DateTimeField(_("activated at"), null=True, blank=True)
  fixed = ext.BooleanField(_("fixed"), default=False,
                       help_text=_("If true, This field will not affected on bulk activation/deactivation processes"))

  class Meta:
    abstract = True

  def activate(self):
    activate(self)

  def deactivate(self):
    deactivate(self)