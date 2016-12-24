from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication as RestTokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from . import models

class TokenAuthentication(RestTokenAuthentication):
  model = models.Token

  def authenticate_credentials(self, key):
    model = self.get_model()
    try:
      token = model.objects.select_related('user').get(key=key, active=True)
    except model.DoesNotExist:
      raise AuthenticationFailed(_("Invalid token."))

    if not token.user.is_active:
      raise AuthenticationFailed(_("User inactive or deleted"))

    return (token.user, token)