from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ScpcAuthConfig(AppConfig):
    name = 'scpc_auth'
    verbose_name = _("SCPC :: Auth")
