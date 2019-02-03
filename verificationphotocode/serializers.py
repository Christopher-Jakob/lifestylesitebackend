from rest_framework import serializers
from models import *


class VerificationPhotoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationPhotoCode
        fields = ('__all__')
