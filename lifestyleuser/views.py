# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from swingers.models import Swinger
from models import *
from rest_framework import status
from hosts.models import Hosts
from serializers import Usersignupserializer, SwingerSignupserializer
from settingsandattributes.models import *
from django.db import IntegrityError
from transmission.email.validation.emailvalidation import validateemail
from transmission.email.signups.signupemails import sendemail


# Create your views here.


# used for declineing or accepting a swinger application
class SwingerDeclineAcceptView(APIView):
    

# used for swinger signup

class SwingerUserSignup(APIView):

    def post(self, request, *args, **kwargs):
        print('fuck you mother fucker')
        data = SwingerSignupserializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            email = data.get('email')
            active = data.get('is_active')
            prelaunchsignup = data.get('prelaunchsignup')
            expandtoareaemail = data.get('expandtoareaemail')
            if expandtoareaemail != None:
                print('this is a swinger request signup')
                expandtoareacountry = data.get('expandtoareacountry')
                country = get_object_or_404(Country, pk=expandtoareacountry)
                expandtoareastate = data.get('expandtoareastate')
                state = get_object_or_404(State, pk=expandtoareastate)
                expandtoareacity = data.get('expandtoareacity')
                city = get_object_or_404(City, pk=expandtoareacity)
                validation = validateemail(expandtoareaemail)
                validationjson = validation.json()
                validemail = (validationjson['is_valid'])
                isdisposableemail = (validationjson['is_disposable_address'])
                failcontext = ''
                failedvalidation = False
                if not validemail:
                    failcontext = failcontext + 'This email is not a valid email. '
                    failedvalidation = True
                if isdisposableemail:
                    failcontext = failcontext + 'Disposable Email addresses cannot be used. '
                    failedvalidation = True

                if failedvalidation:
                    return Response({
                        'failcontext': failcontext
                    },
                        status=status.HTTP_400_BAD_REQUEST)

                try:
                    print('its trying to create a user with request')
                    user = LifestyleUser.objects.create_user(email=email, is_active=active, isswinger=True ,
                                                             prelaunchsignup = prelaunchsignup)
                    swingpreference = data.get('swingertype')
                    swingpreference = get_object_or_404(SwingPreference, pk=swingpreference)
                    swinger = Swinger(user=user, swingertype=swingpreference, country=country,
                                      state=state, city=city)
                    swinger.save()
                    sendemail('swingeractivecitysignup.html',email)


                    return Response(status=status.HTTP_201_CREATED)
                except IntegrityError:
                    failcontext = failcontext + 'That email is already in use'
                    return Response({
                        'failcontext': failcontext
                    },
                        status=status.HTTP_400_BAD_REQUEST)




            if email != None:
                print('this is a swinger full sign up')
                country = data.get('country')
                country = get_object_or_404(Country, pk=country)
                state = data.get('state')
                state = get_object_or_404(State, pk=state)
                city = data.get('city')
                city = get_object_or_404(City, pk=city)
                validation = validateemail(email)
                validationjson = validation.json()
                validemail = (validationjson['is_valid'])
                isdisposableemail = (validationjson['is_disposable_address'])
                failcontext = ''
                failedvalidation = False
                if not validemail:
                    failcontext = failcontext + 'This email is not a valid email. '
                    failedvalidation = True
                if isdisposableemail:
                    failcontext = failcontext + 'Disposable Email addresses cannot be used. '
                    failedvalidation = True

                if failedvalidation:
                    return Response({
                        'failcontext': failcontext
                    },
                        status=status.HTTP_400_BAD_REQUEST)

                try:
                    print('user is being created in full')
                    user = LifestyleUser.objects.create_user(email=email, is_active=active, isswinger=True,
                                                             prelaunchsignup=prelaunchsignup)
                    swingpreference = data.get('swingertype')
                    swingpreference = get_object_or_404(SwingPreference, pk=swingpreference)
                    username = data.get('username')
                    sex1 = data.get('sex1')
                    sex2 = data.get('sex2')
                    birthday1 = data.get('birthdayone')
                    verificationphotocode = data.get('verificationphotocode')
                    birthday2 = data.get('birthdaytwo')
                    ethnicity1 = data.get('ethnicity1')
                    ethnicity1 = get_object_or_404(SwingerEthnicgroups, pk=ethnicity1)
                    ethnicity2 = data.get('ethnicity2')
                    if ethnicity2 != None:
                        ethnicity2 = get_object_or_404(SwingerEthnicgroups, pk=ethnicity2)

                    verificationphoto = data.get('verificationphoto')
                    verificationphotokey = data.get('verificationphotokey')

                    swinger = Swinger(user=user, swingertype=swingpreference, country=country,
                                      state=state, city=city, username=username, sex1=sex1, sex2=sex2,
                                      birthday1=birthday1, birthday2=birthday2, ethnicity1=ethnicity1,
                                      ethnicity2=ethnicity2, verificationphoto=verificationphoto, verificationphotokey=verificationphotokey, verificationphotocode= verificationphotocode

                                      )
                    swinger.save()
                    sendemail('swingeractivecitysignup.html', email)

                    return Response(status=status.HTTP_201_CREATED)
                except IntegrityError:
                    failcontext = failcontext + 'That email is already in use'
                    return Response({
                        'failcontext': failcontext
                    },
                        status=status.HTTP_400_BAD_REQUEST)


# used for pre launch landing page sign up
class LifeStyleUser(APIView):

    def post(self, request, *args, **kwargs):
        data = Usersignupserializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            email = data.get('email')
            # validate email
            validation = validateemail(email)
            validationjson = validation.json()
            validemail = (validationjson['is_valid'])
            isdisposableemail = (validationjson['is_disposable_address'])
            failcontext = ''
            failedvalidation = False
            if not validemail:
                failcontext = failcontext + 'This email is not a valid email. '
                failedvalidation = True
            if isdisposableemail:
                failcontext = failcontext + 'Disposable Email addresses cannot be used. '
                failedvalidation = True

            if failedvalidation:
                return Response({
                    'failcontext': failcontext
                },
                status=status.HTTP_400_BAD_REQUEST)

            hostsignup = data.get('hostsignup')
            swingersignup = data.get('swingersignup')
            prelaunchsignup = data.get('prelaunchsignup')
            active= data.get('active')
            country = data.get('country')
            state = data.get('state')
            city = data.get('city')
            country = get_object_or_404(Country, pk=country)
            state = get_object_or_404(State, pk=state)
            city = get_object_or_404(City, pk=city)


            if swingersignup:
                try:
                    user = LifestyleUser.objects.create_user(email=email, is_active=active, isswinger=True ,
                                                             prelaunchsignup = prelaunchsignup)
                    swingpreference = data.get('swingerpreference')
                    swingpreference = get_object_or_404(SwingPreference, pk=swingpreference)
                    swinger = Swinger(user=user, swingertype=swingpreference, country=country,
                                      state=state, city=city)
                    swinger.save()
                    sendemail('swingeractivecitysignup.html',email)


                    return Response(status=status.HTTP_201_CREATED)
                except IntegrityError:
                    failcontext = failcontext + 'That email is already in use'
                    return Response({
                        'failcontext': failcontext
                    },
                        status=status.HTTP_400_BAD_REQUEST)

            if hostsignup:
                try:

                    user = LifestyleUser(email=email, is_active=active, ishost=True , prelaunchsignup = prelaunchsignup)
                    user.save()
                    host = data.get('hosttype')
                    hosttype = get_object_or_404(HostTypes, pk=host)
                    host = Hosts(user=user, hosttype=hosttype, country=country, state=state,
                                     city=city)
                    host.save()
                    sendemail('hostactivecitysignup.html', email)

                    return Response(status=status.HTTP_201_CREATED)
                except IntegrityError:
                    failcontext = failcontext + 'That email is already in use'
                    return Response({
                        'failcontext': failcontext
                    },
                    status=status.HTTP_400_BAD_REQUEST)















