# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# this is just for now for the site admin while we are taking pre launch sign ups

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)


class PasswordValidate(APIView):
    def post(self, request, *args, **kwargs):
        data = PasswordSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            validdata = data.validated_data
            password = validdata.get('password')
            if password == 'zaq11qaz':
                return Response({
                    'status': 1
                })
            return Response({
                'status': 0
            })