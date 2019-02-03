# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from serializers import *
from models import *
from settingsandattributes.models import *


class SwingerSignupView(APIView):

    def post(self, request, *args, **kwargs):
        serialized = Swingersignupserializer(data=request.data)
        if serialized.is_valid(raise_exception = True):
            validdata = serialized.validated_data
            email = validdata.get('email')
            swingertype = validdata.get('swingertype')
            swingertype = get_object_or_404(SwingPreference, pk=swingertype)
            country = validdata.get('country')
            country = get_object_or_404(Country, pk=country)
            state = validdata.get('state')
            state = get_object_or_404(State, pk=state)
            city = validdata.get('city')
            city = get_object_or_404(City, pk=city)
            active =validdata.get('active')
            swinger = Swinger(email=email, swingertype=swingertype, country=country,
                                   state=state, city=city, active=active)
            swinger.save()


