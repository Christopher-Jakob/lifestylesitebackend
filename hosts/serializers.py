from rest_framework import serializers
from lifestyleuser.serializers import UserSerializer
from settingsandattributes.serializers import *
from hosts.models import Hosts


class HostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    hosttype = HostTypeSerializer()
    country = CountrySerializer()
    state = StateSerializer()
    city = CitySerializer()
    class Meta:
        model = Hosts
        fields=('user','hosttype', 'country','state', 'city')
