from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from serializers import LifestyleUserSerializer
from models import LifestyleUser


class ModifyLifestyleUser(APIView):

    def put(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(LifestyleUser, pk=instance)
        serializerdata = LifestyleUserSerializer(instance, data=request.data, partial=True)
        if serializerdata.is_valid(raise_exception=True):
            serializerdata.save()
            return Response(serializerdata.data)



