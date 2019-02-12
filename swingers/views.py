from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from serializers import *
from models import *
from rest_framework import status

class GetAllSwingers(APIView):
    
    def get(self, request, *args, **kwargs):
        swingers = Swinger.objects.all()
        serialized = SwingerSerializer(swingers, many=True)
        return Response(serialized.data)



class ModifySwinger(APIView):
    def put(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(Swinger, pk=instance)
        serializeddata = SwingPreferenceSerializer(instance, data=request.data, partial=True)
        if serializeddata.is_valid(raise_exception=True):
            serializeddata.save()
            return Response(serializeddata.data)
