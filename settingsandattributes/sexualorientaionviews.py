# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status




class PostGetAllSexualOrientation(APIView):

    def post(self, request, *args, **kwargs):
        data = SexualOrientationSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            sexualorientation = SexualOrientation(**data)
            sexualorientation.save()
            serialized = SexualOrientationSerializer(sexualorientation)
            return Response(serialized.data)

    def get(self,request, *args, **kwargs):
        sexualorientation = SexualOrientation.objects.all()
        serialized = SexTypeSerializer(sexualorientation, many=True)
        return Response(serialized.data)


class SexualOrientationDetail(APIView):

    def get(self, request, *args, **kwargs):
        sextypepk = kwargs.get('pk')
        sexualorientation = get_object_or_404(SexualOrientation, pk=sextypepk)
        serialized = SexTypeSerializer(sexualorientation)
        return Response(serialized)

    def put(self, request, *args, **kwargs):
        sextypepk = kwargs.get('pk')
        instance = get_object_or_404(SexualOrientation, pk=sextypepk)
        serialzeddata = SexualOrientationSerializer(instance, data=request.data, partial=True)
        if serialzeddata.is_valid(raise_exception=True):
            serialzeddata.save()
            return Response(serialzeddata.data)

    def delete(self, request, *args, **kwargs):
        sextypepk = kwargs.get('pk')
        instance = get_object_or_404(SexualOrientation, pk=sextypepk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)