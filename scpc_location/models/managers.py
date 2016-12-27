from django.db.models.manager import Manager

from scpc.utils import setallattr
from scpc_core.models.managers import get_now

class LastKnowLocationManager(Manager):

  def register_location(self, user, **kwargs):
    now = get_now()

    try:
      last_location = self.get(user=user)
    except self.model.DoesNotExist:
      last_location = self.model()
      last_location.created_at = now

    last_location.user = user
    last_location.updated_at = now
    setallattr(last_location, **kwargs)
    last_location.save()
    return last_location