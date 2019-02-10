from rest_framework import serializers
from models import LifestyleUser


# used on the landing page pre launch
class Usersignupserializer(serializers.Serializer):
    country = serializers.IntegerField()
    state = serializers.IntegerField()
    city = serializers.IntegerField()
    active = serializers.BooleanField(default=False)
    hostsignup = serializers.BooleanField(default=False)
    swingerpreference = serializers.IntegerField(allow_null=True)
    hosttype = serializers.IntegerField(allow_null =True)
    swingersignup = serializers.BooleanField(default=False)
    email = serializers.EmailField()
    prelaunchsignup = serializers.BooleanField(default=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifestyleUser
        fields = ('__all__')

# used when user is signing up as a swinger
class SwingerSignupserializer(serializers.Serializer):
    country = serializers.IntegerField(allow_null=True)
    state = serializers.IntegerField(allow_null=True)
    city = serializers.IntegerField(allow_null=True)
    expandtoareaemail = serializers.EmailField(allow_null=True)
    expandtoareacountry = serializers.IntegerField(allow_null=True)
    expandtoareastate = serializers.IntegerField(allow_null=True)
    expandtoareacity = serializers.IntegerField(allow_null=True)
    username = serializers.CharField(max_length=100, allow_null=True)
    email = serializers.EmailField(allow_null=True)
    is_active = serializers.BooleanField(default=False)
    password = serializers.CharField(max_length=100, allow_null=True)
    swingertype = serializers.IntegerField(allow_null=True)
    birthdayone = serializers.DateField(allow_null=True)
    birthdaytwo = serializers.DateField(allow_null=True)
    ethnicity1 = serializers.IntegerField(allow_null=True)
    ethnicity2 = serializers.IntegerField(allow_null=True)
    verificationphoto = serializers.CharField(max_length=300)
    verificationphotokey = serializers.CharField(max_length=300)
    prelaunchsignup = serializers.BooleanField(default=False)




