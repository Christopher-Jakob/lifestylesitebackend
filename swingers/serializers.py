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
        fields = ('user', 'pk','swingertype', 'headline', 'country', 'maxdistance5', 'maxdistance10', 'maxdistance20', 'maxdistance35', 'maxdistance60',
                  'state', 'city', 'username', 'sex1', 'sex2', 'maxdistance100', 'maxdistance150', 'maxdistance300','maxdistance600',
                  'maxdistanceany','birthday1', 'birthday2', 'ethnicity1', 'ethnicity2', 'orientation1', 'orientation2',
                  'verificationphoto', 'verificationphotokey', 'verificationphotocode','istranny',
                  'isstraightman','isbisexualman','ishetroflexibleman','isgayman', 'isstraightwoman',
                  'isbisexualwoman', 'ishetroflexiblewoman', 'islesbianwoman', 'wantstranny',
                  'wantsinglewoman', 'wantsingleman', 'wantsinglets', 'wantcouplemanwoman', 'wantcouplewomanwoman',
                  'wantcouplewomants', 'wantcouplemanman', 'wantcouplemants', 'wantcoupletsts',
                  'wantsstraightman', 'wantsbisexualman','wantshetroflexibleman','wantsgayman',
                  'wantsstraightwoman','wantsbisexualwoman','wantshetroflexiblewoman','wantslesbianwoman',
                  'wanthispanic', 'wantlatino', 'wantwhite', 'wantwhite', 'wantblack', 'wantwhite', 'wantsthinbodytype',
                  'wantscurvybodytype','wantasian', 'wantnativeamerican', 'wantpacificislander', 'minpreferedage', 'maxpreferedage',
                  'bodytypeverificationphoto','bodytypeverificationphotokey','bodytypeverificationphotocode',
                  'optinbodytypefiltering','isbodybuilderbodytype1','isathleticbodytype1','isaveragebodytype1',
                  'isthinbodytype1', 'iscurvybodytype1', 'isafewextrapoundsbodytype1', 'isheavysetbodytype1','isbodybuilderbodytype2',
                  'isathleticbodytype2', 'isthinbodytype2', 'iscurvybodytype2','isaveragebodytype2','isafewextrapoundsbodytype2',
                  'isheavysetbodytype2','wantsbodybuilderbodytype','wantsathleticbodytype','wantsaveragebodytype',
                  'wantsafewextrapoundsbodytype','wantsheavysetbodytype','allownonoptinbodytypeusers',
                  'bodytypesubmissiondate','bodytypeawaitingdecision','bodytypefilteractive', 'profilephoto',
                  'profilephotokey', 'coverphoto', 'coverphotokey')



class UpdateLocationSerializer(serializers.Serializer):
    country = serializers.IntegerField()
    state = serializers.IntegerField()
    city = serializers.IntegerField()
