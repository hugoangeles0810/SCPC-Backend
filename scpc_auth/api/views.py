from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from scpc_auth.models import Token
from scpc_auth.api import serializers
from scpc_core.models import User
from scpc_auth.exceptions import EmailAlreadyRegisteredException

class EmailRegistrationAPIView(APIView):

  def post(self, request):
    """
    Registra un usuario por email y password
    ---
    request_serializer: serializers.EmailRegistration
    response_serializer: serializers.TokenGenerationResponse
    """
    serializer = serializers.EmailRegistration(data=request.data)
    serializer.is_valid(True)
    data = serializer.validated_data
    try:
      data['username'] = data['email']
      user = User.objects.create_user(**data)
      token = Token.objects.create(user=user)
      rdata = serializers.TokenGenerationResponse(token)
      return Response(data=rdata.data)
    except EmailAlreadyRegisteredException as e:
      return Response(data=e.code, status=HTTP_400_BAD_REQUEST)


class EmailLoginAPIView(APIView):

  def post(self, request):
    """
    Obtiene un token de autenticación en base al email y el password
    ---
    request_serializer: serializers.EmailRegistration
    response_serializer: serializers.TokenGenerationResponse
    """
    serializer = serializers.EmailRegistration(data=request.data)
    serializer.is_valid(True)
    data = serializer.validated_data
    user = authenticate(username=data.get('email'), password=data.get('password'))
    if user:
      token = Token.objects.create(user=user)
      rdata = serializers.TokenGenerationResponse(token)
      return Response(data=rdata.data)
    else:
      return Response(status=HTTP_401_UNAUTHORIZED)