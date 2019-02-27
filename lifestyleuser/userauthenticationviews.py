# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from lifestyleuser.serializers import LifestyleUserSerializer
from models import *



# gets the base lifestyle user object of self user
class UserGetSelf(APIView):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(LifestyleUser, pk=request.user.pk)
        serializer = LifestyleUserSerializer(user)
        return Response(serializer.data)



