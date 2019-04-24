# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from lifestyleuser.models import LifestyleUser
from serializers import ChecksandVerificationsSerializer

# Create your views here.

class EmailNotTaken(APIView):

    def post(self, request, *args, **kwargs):
        serialized = ChecksandVerificationsSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            data = serialized.validated_data
            email = data.get('email')
            try:
                user = LifestyleUser.objects.get(email=email)
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            except IntegrityError:
                return Response(status=status.HTTP_200_OK)
            except LifestyleUser.DoesNotExist:
                return Response(status=status.HTTP_200_OK)

class VerifyPassword(APIView):
    def post(self, request, *args, **kwargs):
        userpk = kwargs.get('pk')
        serialized = ChecksandVerificationsSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            print('valid serialized')
            data = serialized.validated_data
            currentpassword = data.get('currentpassword')
            user = get_object_or_404(LifestyleUser, pk=userpk)
            print('this is the password')
            print(currentpassword)
            validpassword = user.check_password(currentpassword)
            if validpassword:
                return Response(status=status.HTTP_200_OK)
            if not validpassword:
                return Response(status=status.HTTP_400_BAD_REQUEST)





