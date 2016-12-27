from rest_framework import serializers as ext

class UserLocationRequest(ext.Serializer):
  latitude = ext.DecimalField(max_digits=12, decimal_places=9)
  longitude = ext.DecimalField(max_digits=12, decimal_places=9)