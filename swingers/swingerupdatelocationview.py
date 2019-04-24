# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from serializers import *
from models import *
from settingsandattributes.models import *


# updates the location of a swinger and returns a swinger object
class SwingerUpdateLocation(APIView):

    def put(self, request, *args, **kwargs):
        swingerpk = kwargs.get('pk')
        data = UpdateLocationSerializer(data=request.data)
        if data.is_valid(raise_exception =True):
            data = data.validated_data
            swinger = get_object_or_404(Swinger, pk=swingerpk)
            country = data.get('country')
            state = data.get('state')
            city = data.get('city')
            country = get_object_or_404(Country, pk=country)
            state = get_object_or_404(State, pk=state)
            city = get_object_or_404(City, pk=city)
            swinger.country = country
            swinger.state = state
            swinger.city = city
            swinger.save()
            serializedswinger = SwingerSerializer(swinger)
            return Response(serializedswinger.data)



