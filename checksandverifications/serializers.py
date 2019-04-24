from rest_framework import serializers


class ChecksandVerificationsSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    currentpassword = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)


