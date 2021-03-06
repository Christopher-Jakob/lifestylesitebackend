from rest_framework import serializers
from lifestyleuser.serializers import UserSerializer
from settingsandattributes.serializers import *
from models import *


class SwingerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    swingertype = SwingPreferenceSerializer()
    country = CountrySerializer()
    state = StateSerializer()
    city = CitySerializer()

    class Meta:
        model = Swinger
        fields = ('user', 'swingertype', 'country', 'state', 'city', 'username', 'sex1', 'sex2',
                  'birthday1', 'birthday2', 'ethnicity1', 'ethnicity2', 'verificationphoto', 'verificationphotokey', 'verificationphotocode')




