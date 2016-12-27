from rest_framework import views as ext
from rest_framework.permissions import IsAuthenticated

class AuthenticatedAPIView(ext.APIView):
    permission_classes = (IsAuthenticated,)
