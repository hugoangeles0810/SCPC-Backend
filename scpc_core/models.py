
from django.contrib.auth.models import AbstractUser
from django.db import models as ext
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
  class Meta(AbstractUser.Meta):
    swappable = "AUTH_USER_MODEL"

class Request(ext.Model):
  user = ext.ForeignKey(User, related_name='requests', null=True, blank=True)
  ip_address = ext.CharField(_("ip address"), max_length=255, null=True, blank=True)
  url = ext.CharField(_("url"), max_length=255, null=True, blank=True)
  method = ext.CharField(_("method"), max_length=255, null=True, blank=True)
  request_headers = ext.TextField(_("request headers"), null=True, blank=True)
  request_body = ext.TextField(_("request body"), null=True, blank=True)
  response_status = ext.IntegerField(_("response status"), null=True, blank=True)
  validation_errors = ext.TextField(_("validation erros"), null=True, blank=True)
  started_at = ext.DateTimeField(_("started at"), null=True, blank=True)
  finished_at = ext.DateTimeField(_("finished at"), null=True, blank=True)


  class Meta:
    verbose_name = _("request")
    verbose_name_plural = _("requests")

  def __str__(self):
    return self.ip_address + " | " + self.method + " | " + self.url