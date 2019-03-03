from rest_framework import serializers
from lifestyleuser.serializers import *
from settingsandattributes.serializers import *
from models import *


class SwingerSerializer(serializers.ModelSerializer):
    swingertype = SwingPreferenceSerializer()
    country = CountrySerializer()
    state = StateSerializer()
    city = CitySerializer()
    sex1 = SexTypeSerializer()
    sex2 = SexTypeSerializer()
    orientation1 = SexualOrientationSerializer()
    orientation2 = SexualOrientationSerializer()
    ethnicity1 = SwingerEthnicgroupSerializer()
    ethnicity2 = SwingerEthnicgroupSerializer()

    class Meta:
        model = Swinger
        fields = ('user', 'pk','swingertype', 'country', 'state', 'city', 'username', 'sex1', 'sex2',
                  'birthday1', 'birthday2', 'ethnicity1', 'ethnicity2', 'orientation1', 'orientation2',
                  'verificationphoto', 'verificationphotokey', 'verificationphotocode',
                  'wantsinglewoman', 'wantsingleman', 'wantsinglets', 'wantcouplemanwoman', 'wantcouplewomanwoman',
                  'wantcouplewomants', 'wantcouplemanman', 'wantcouplemants', 'wantcoupletsts',
                  'wanthispanic', 'wantlatino', 'wantwhite', 'wantwhite', 'wantblack', 'wantwhite',
                  'wantasian', 'wantnativeamerican', 'wantpacificislander', 'minpreferedage', 'maxpreferedage')




