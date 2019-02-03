# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


class PostGetallSwingerEthnictypes(APIView):

    def post(self, request, *args, **kwargs):
        data = SwingerEthnicgroupSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            ethnicgroup = SwingerEthnicgroups(**data)
            ethnicgroup.save()
            serialized = SwingerEthnicgroupSerializer(ethnicgroup)
            return Response(serialized.data)


    def get(self, request, *args, **kwargs):
        ethnicgroups = SwingerEthnicgroups.objects.all()
        serialized = SwingerEthnicgroupSerializer(ethnicgroups, many=True)
        return Response(serialized.data)



class SwingerEthnictypedetail(APIView):

    def get(self, request, *args, **kwargs):
        ethnictypespk = kwargs.get('pk')
        instance = get_object_or_404(SwingerEthnicgroups, pk=ethnictypespk)
        serialized = SwingerEthnicgroupSerializer(instance)
        return Response(serialized.data)

    def put(self, request, *args, **kwargs):
        ethnictypepk = kwargs.get('pk')
        instance = get_object_or_404(SwingerEthnicgroups, pk=ethnictypepk)
        serializeddata = SexTypeSerializer(instance, data=request.data, partial=True)
        if serializeddata.is_valid(raise_exception=True):
            serializeddata.save()
            return Response(serializeddata.data)

    def delete(self, request, *args, **kwargs):
        ethnicpk = kwargs.get('pk')
        instance = get_object_or_404(SwingerEthnicgroups, pk=ethnicpk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)



