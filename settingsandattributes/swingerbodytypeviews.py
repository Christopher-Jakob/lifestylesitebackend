# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status




class PostGetAllSwingerBodyTypes(APIView):

    def post(self, request, *args, **kwargs):
        data = SwingerBodyTypeSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            bodytype = SwingerBodyTypes(**data)
            bodytype.save()
            serialized = SwingerBodyTypeSerializer(bodytype)
            return Response(serialized.data)

    def get(self,request, *args, **kwargs):
        bodytypes = SwingerBodyTypes.objects.all()
        serialized = SwingerBodyTypeSerializer(bodytypes, many=True)
        return Response(serialized.data)


class SwingerBodyTypeDetail(APIView):

    def get(self, request, *args, **kwargs):
        bodytypepk = kwargs.get('pk')
        swingerbodytype = get_object_or_404(SwingerBodyTypes, pk=bodytypepk)
        serialized = SwingerBodyTypeSerializer(swingerbodytype)
        return Response(serialized)

    def put(self, request, *args, **kwargs):
        bodytypepk = kwargs.get('pk')
        instance = get_object_or_404(SwingerBodyTypes, pk=bodytypepk)
        serialzeddata = SwingerBodyTypeSerializer(instance, data=request.data, partial=True)
        if serialzeddata.is_valid(raise_exception=True):
            serialzeddata.save()
            return Response(serialzeddata.data)

    def delete(self, request, *args, **kwargs):
        bodytypepk = kwargs.get('pk')
        instance = get_object_or_404(SwingerBodyTypes, pk=bodytypepk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)