from rest_framework import serializers as ext


class RegisterByAccessTokenData(ext.Serializer):
    access_token = ext.CharField()


class TokenGenerationResponse(ext.Serializer):
    email = ext.EmailField(source='user.email')
    token = ext.CharField(source='key')


class EmailRegistration(ext.Serializer):
    email = ext.EmailField()
    password = ext.CharField()