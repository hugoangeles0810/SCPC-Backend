from django.db import models as ext
from django.utils.translation import gettext_lazy as _

from scpc_core.models import User
from scpc_location.models import managers

class LastUserLocation(ext.Model):
  user = ext.ForeignKey(User, related_name='locations', null=True, blank=True)
  latitude = ext.DecimalField(_("latitude"), null=False, blank=False, max_digits=12, decimal_places=9)
  longitude = ext.DecimalField(_("longitude"), null=False, blank=False, max_digits=12, decimal_places=9)
  created_at = ext.DateTimeField(_("created at"), null=True, blank=True)
  updated_at = ext.DateTimeField(_("updated at"), null=True, blank=True)

  objects = managers.LastKnowLocationManager()

  class Meta:
    verbose_name = _("Last User Location")
    verbose_name_plural = _("Last User Locations")