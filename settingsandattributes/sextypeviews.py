# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

class PostGetAllSexTypes(APIView):

    def post(self, request, *args, **kwargs):
        data = SexTypeSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            sextype = SexType(**data)
            sextype.save()
            serialized = SexTypeSerializer(sextype)
            return Response(serialized.data)

    def get(self,request, *args, **kwargs):
        sextypes = SexType.objects.all()
        serialized = SexTypeSerializer(sextypes, many=True)
        return Response(serialized.data)


class SexTypeDetail(APIView):

    def get(self, request, *args, **kwargs):
        sextypepk = kwargs.get('pk')
        sextype = get_object_or_404(SexType, pk=sextypepk)
        serialized = SexTypeSerializer(sextype)
        return Response(serialized)

    def put(self, request, *args, **kwargs):
        sextypepk = kwargs.get('pk')
        instance = get_object_or_404(SexType, pk=sextypepk)
        serialzeddata = SexTypeSerializer(instance, data=request.data, partial=True)
        if serialzeddata.is_valid(raise_exception=True):
            serialzeddata.save()
            return Response(serialzeddata.data)

    def delete(self, request, *args, **kwargs):
        sextypepk = kwargs.get('pk')
        instance = get_object_or_404(SexType, pk=sextypepk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)

