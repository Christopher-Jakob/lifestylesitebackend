from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from serializers import LifestyleUserSerializer, NewPasswordSerializer
from models import LifestyleUser

class UserChangePassword(APIView):
    def put(self, request, *args, **kwargs):
        userpk = kwargs.get('pk')
        user = get_object_or_404(LifestyleUser, pk=userpk)
        data = NewPasswordSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.validated_data
            password = data.get('password')
            user.set_password(password)
            user.save()
            return Response(status=status.HTTP_200_OK)