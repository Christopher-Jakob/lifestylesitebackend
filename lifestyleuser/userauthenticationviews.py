# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from lifestyleuser.serializers import LifestyleUserSerializer
from models import *
from swingers.models import Swinger
from swingers.serializers import SwingerSerializer
from rest_framework import status


# gets the base lifestyle user object of self user
class UserGetSelf(APIView):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(LifestyleUser, pk=request.user.pk)
        serializer = LifestyleUserSerializer(user)
        return Response(serializer.data)

# gets the swinger user object of self user

class SwingerGetSelf(APIView):

    def get(self, request, *args, **kwargs):
        userpk = kwargs.get('pk')
        lifestyleuser = get_object_or_404(LifestyleUser, pk=userpk)
        swingeruser = get_object_or_404(Swinger, user=lifestyleuser)
        serializeduser = SwingerSerializer(swingeruser)
        return Response(serializeduser.data)


