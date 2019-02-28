from rest_framework import serializers
from models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('__all__')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('__all__')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')

class SexTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexType
        fields=('__all__')

class PostPutSwingPreferenceSerializer(serializers.ModelSerializer):
    sex1 = serializers.IntegerField()
    sex2 = serializers.IntegerField(allow_null=True)
    class Meta:
        model = SwingPreference
        fields = ('sex1', 'sex2', 'couple', 'name')

class SwingPreferenceSerializer(serializers.ModelSerializer):
    sex1 = SexTypeSerializer()
    sex2 = SexTypeSerializer()
    class Meta:
        model = SwingPreference
        fields = ('sex1', 'sex2', 'couple', 'name', 'id')

class HostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostTypes
        fields = ('__all__')

class SwingerEthnicgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwingerEthnicgroups
        fields = ('__all__')

class SwingerSignupDeclineReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwingerSignupDeclineReason
        fields = ('__all__')

class SexualOrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexualOrientation
        fields = ('__all__')

class SwingerBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwingerBodyTypes
        fields = ('__all__')