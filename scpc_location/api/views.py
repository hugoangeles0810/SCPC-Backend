from rest_framework.response import Response
from scpc.api import views

from scpc.utils import setallattr
from scpc_core.models.managers import get_now
from scpc_location.api import serializers
from scpc_location.models import LastUserLocation

class UpdateUserLocationView(views.AuthenticatedAPIView):

  def post(self, request):
    """
    Registra el cambio de geoposición del usuario
    request_serializer: serializers.UserLocationRequest
    """
    serializer = serializers.UserLocationRequest(data=request.data)
    serializer.is_valid(True)
    data = serializer.validated_data
    LastUserLocation.objects.register_location(request.user, **data)
    return Response(data={"success": True})