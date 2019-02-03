from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import *
from models import *
from rest_framework import status

class GetAllSwingers(APIView):
    
    def get(self, request, *args, **kwargs):
        swingers = Swinger.objects.all()
        serialized = SwingerSerializer(swingers, many=True)
        return Response(serialized.data)

