# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from models import Hosts
from serializers import *
from rest_framework import status



# Create your views here.

class GetAllHosts(APIView):

    def get(self, request, *args, **kwargs):
        hosts = Hosts.objects.all()
        serialized = HostSerializer(hosts, many=True)
        return Response(serialized.data)



