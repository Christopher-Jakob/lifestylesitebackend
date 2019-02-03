# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# get all host types or create a host type edit delete
class HostTypeGetPutDeleteView(APIView):

    def get(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(HostTypes, pk=instance)
        instance = HostTypeSerializer(instance)
        return Response(instance.data)

    def put(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(HostTypes, pk=instance)
        serializeddata = HostTypeSerializer(instance, data=request.data, partial=True)
        if serializeddata.is_valid(raise_exception=True):
            serializeddata.save()
            return Response(serializeddata.data)


    def delete(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(HostTypes, pk=instance)
        instance.delete()
        return Response(status=status.HTTP_200_OK)


# get specific host type
class GetAllCreateHostType(APIView):

    def get(self, request, *args, **kwargs):
        hostypes = HostTypes.objects.all()
        hostypes = HostTypeSerializer(hostypes, many=True)
        return Response(hostypes.data)

    def post(self, request, *args, **kwargs):
        # authorization goes here
        data = HostTypeSerializer(data= request.data)
        if data.is_valid(raise_exception=True):
            validdata = data.validated_data
            type = HostTypes(**validdata)
            type.save()
            createdtype = HostTypeSerializer(type)
            return Response(createdtype.data)


