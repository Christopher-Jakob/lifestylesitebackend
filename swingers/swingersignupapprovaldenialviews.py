# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from lifestyleuser.models import LifestyleUser
from serializers import *
from models import *
from settingsandattributes.models import *



class SwingerApprovalListGet(APIView):

    def get(self,request, *args, **kwargs):
        swingers = Swinger.objects.filter(user__in = LifestyleUser.objects.filter(isswinger=True, isswingerapproved=False))
        serializedswingers = SwingerSerializer(swingers, many=True)
        return Response(serializedswingers.data)
