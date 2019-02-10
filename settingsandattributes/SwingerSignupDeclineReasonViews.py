# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


class SwingerSignupDeclineReasonView(APIView):

    def get(self, request,*args, **kwargs):
        reasons = SwingerSignupDeclineReason.objects.all()
        serialized = SwingerSignupDeclineReasonSerializer(reasons, many=True)
        return Response(serialized.data)

    def post(self, request, *args, **kwargs):
        data = SwingerSignupDeclineReasonSerializer(data = request.data)
        if data.is_valid(raise_exception=True):
            validdata = data.validated_data
            reason = SwingerSignupDeclineReason(**validdata)
            reason.save()
            createdreason = SwingerSignupDeclineReasonSerializer(reason)
            return Response(createdreason.data)

class DeleteSwingerSignupDeclineReasonView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(SwingerSignupDeclineReason, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_200_OK)