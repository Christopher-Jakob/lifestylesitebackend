# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from serializers import *
from models import *
from rest_framework import status
import random

# Create your views here.

class VerificationPhotoCodeview(APIView):

    def post(self, request, *args, **kwargs):
        number = random.randint(100000, 999999)
        code = VerificationPhotoCode(code=number)
        code.save()
        serialized = VerificationPhotoCodeSerializer(code)
        return Response(serialized.data)

    def get(self,request, *args, **kwargs):
        pk = kwargs.get('pk')
        code = kwargs.get('code')
        instance = get_object_or_404(VerificationPhotoCode, pk=pk, code=code)
        return Response(status=status.HTTP_200_OK)



    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        code = kwargs.get('code')
        instance = get_object_or_404(VerificationPhotoCode, pk=code, code=code )
        instance.delete()
        return Response(status=status.HTTP_200_OK)



