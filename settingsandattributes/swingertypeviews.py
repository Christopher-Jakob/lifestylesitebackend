# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# get all swinger types or create a swinger type edit delete
class SwingerTypeDetailView(APIView):

    def get(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(SwingPreference, pk=instance)
        instance = SwingPreferenceSerializer(instance)
        return Response(instance.data)


    def put(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(SwingPreference, pk=instance)
        serializeddata = SwingPreferenceSerializer(instance, data=request.data, partial=True)
        if serializeddata.is_valid(raise_exception=True):
            serializeddata.save()
            return Response(serializeddata.data)


    def delete(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(SwingPreference, pk=instance)
        instance.delete()
        return Response(status=status.HTTP_200_OK)


# get specific swinger type
class GetSwingerTypeGetAllCreate(APIView):

    def get(self, request, *args, **kwargs):
        swingertype = SwingPreference.objects.all()
        swingertypes = SwingPreferenceSerializer(swingertype, many=True)
        return Response(swingertypes.data)

    def post(self, request, *args, **kwargs):
        # authorization goes here
        data = PostPutSwingPreferenceSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            validdata = data.validated_data
            sex1 = validdata.get('sex1')
            sex1 = get_object_or_404(SexType, pk=sex1)
            sex2 = validdata.get('sex2')
            if sex2 != None:
                sex2 = get_object_or_404(SexType, pk=sex2)
            else:
                sex2 = None
            couple = validdata.get('couple')
            name = validdata.get('name')
            type = SwingPreference(name=name, couple=couple, sex1=sex1, sex2=sex2)
            type.save()
            createdtype = SwingPreferenceSerializer(type)
            return Response(createdtype.data)





