# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status



# gets all countries of active inactive or all
class GetActiveInactiveCountriesView(APIView):

    def get(self, request, *args, **kwargs):
        status = kwargs.get('status', 0)
        if status == 'inactive':
            countries = Country.objects.filter(active=False)
            serialized = CountrySerializer(countries, many=True)
            return Response(serialized.data)
        if status == 'active':
            countries = Country.objects.filter(active=True)
            serialized = CountrySerializer(countries, many=True)
            return Response(serialized.data)
        if status == 'all':
            countries = Country.objects.all()
            serialized = CountrySerializer(countries, many=True)
            return Response(serialized.data)

# gets all states and cities of inactive active or all
class GetActiveInactiveStatesCitiesView(APIView):

    def get(self, request, *args, **kwargs):
        status = kwargs.get('status', 0)
        type = kwargs.get('type', 0)
        relationpk = kwargs.get('relationpk', 0)

        if type == 'state':
            country = get_object_or_404(Country, pk=relationpk)
            if status == 'inactive':
                states = State.objects.filter(country=country, active=False)
            if status == 'active':
                states = State.objects.filter(country=country, active=True)
            if status == 'all':
                states = State.objects.filter(country=country)
            serialized = StateSerializer(states, many=True)
            return Response(serialized.data)

        if type == 'city':
            state = get_object_or_404(State, pk=relationpk)
            if status == 'inactive':
                cities = City.objects.filter(state=state, active=False)
            if status == 'active':
                cities = City.objects.filter(state=state, active=True)
            if status == 'all':
                cities = City.objects.filter(state=state)
            serialized = CitySerializer(cities, many=True)
            return Response(serialized.data)


# create a country
class CreateCountryView(APIView):

    def post(self, request, *args, **kwargs):

        #add authorization later
        data = CountrySerializer(data=request.data)
        if data.is_valid(raise_exception = True):
            data = data.validated_data
            country = Country(**data)
            country.save()
            createdcountry = CountrySerializer(country)
            return Response(createdcountry.data)

# get put delete country
class GetDeletePutCountryView(APIView):

    def get(self, request, *args, **kwargs):

        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(Country, pk=instance)
        serialized = CitySerializer(instance)
        return Response(serialized.data)



    def put(self, request, *args, **kwargs):

        #add authorization later
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(Country, pk=instance)
        serializeddata = CountrySerializer(instance, data=request.data, partial=True)
        if serializeddata.is_valid(raise_exception=True):
            serializeddata.save()
            return Response(serializeddata.data)

    def delete(self, request, *args, **kwargs):
        # add authorization later
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(Country, pk=instance)
        instance.delete()
        return Response(status = status.HTTP_200_OK)


# create state or city
class CreateStateCityView(APIView):

    def post(self, request, *args, **kwargs):
        # add authorization later

        type = kwargs.get('type', 0)

        if type == 'state':
            referencepk = kwargs.get('pk', 0)
            country = get_object_or_404(Country, pk=referencepk)
            data = StateSerializer(data=request.data)
            if data.is_valid(raise_exception = True):
                data = data.validated_data
                state = State(**data)
                state.save()
                serializeddata = StateSerializer(state)
                return Response(serializeddata.data)

        if type == 'city':
            referencepk = kwargs.get('pk', 0)
            state = get_object_or_404(State, pk=referencepk)
            data = CitySerializer(data=request.data)
            if data.is_valid(raise_exception=True):
                data = data.validated_data
                city = City(**data)
                city.save()
                serializeddata = CitySerializer(city)
                return Response(serializeddata.data)



# get put delete state or city
class GetDeletePutStateCityView(APIView):

    def get(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        type = kwargs.get('type', 0)
        if type == 'state':
            state = get_object_or_404(State, pk=instance)
            serialized = StateSerializer(state)
            return Response(serialized.data)
        if type == 'city':
            city = get_object_or_404(City, pk=instance)
            serialized = CitySerializer(city)
            return Response(serialized.data)


    def put(self, request, *args, **kwargs):
        # add authorization later
        type = kwargs.get('type', 0)
        instance = kwargs.get('pk', 0)

        if type == 'state':
            state = get_object_or_404(State, pk = instance)
            serializeddata = StateSerializer(state, data=request.data, partial=True)
            if serializeddata.is_valid(raise_exception=True):
                serializeddata.save()
                return Response(serializeddata.data)

        if type == 'city':
            city = get_object_or_404(City, pk = instance)
            serializeddata = CitySerializer(city, data=request.data, partial=True)
            if serializeddata.is_valid(raise_exception=True):
                serializeddata.save()
                return Response(serializeddata.data)

    def delete(self, request, *args, **kwargs):
        # add authorization later
        type = kwargs.get('type', 0)
        instance = kwargs.get('pk', 0)

        if type == 'state':
            state = get_object_or_404(State, pk=instance)
            state.delete()
            return Response(status=status.HTTP_200_OK)

        if type == 'city':
            city = get_object_or_404(City, pk=instance)
            city.delete()
            return Response(status=status.HTTP_200_OK)


class AllCountriesStatesCities(APIView):

    def get(self, request, *args, **kwargs):
        type = kwargs.get('type')
        if type == 'country':
            countries = Country.objects.all()
            serialized = CountrySerializer(countries, many=True)
            return Response(serialized.data)
        if type == 'state':
            state = State.objects.all()
            serialized = StateSerializer(state, many=True)
            return Response(serialized.data)
        if type == 'city':
            city = City.objects.all()
            serialized = CitySerializer(city, many=True)
            return Response(serialized.data)





