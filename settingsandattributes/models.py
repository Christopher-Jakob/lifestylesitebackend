# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 100)
    active = models.BooleanField(default=False)
    long = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lat = models.DecimalField(max_digits = 20, decimal_places=12, blank=True, null=True)

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    active = models.BooleanField(default=False)
    long = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lat = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    active = models.BooleanField(default=False)
    long = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lat = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)

# the type of sex a person is
class SexType(models.Model):
    name = models.CharField(max_length=100)

class SwingPreference(models.Model):
    name = models.CharField(max_length = 100)
    couple = models.BooleanField(default=False)
    sex1 = models.ForeignKey(SexType, related_name='sex1', on_delete=models.DO_NOTHING, blank=True, null=True)
    sex2 = models.ForeignKey(SexType, related_name='sex2', on_delete=models.DO_NOTHING, blank=True, null=True)



class HostTypes(models.Model):
    name = models.CharField(max_length = 100)


class SwingerEthnicgroups(models.Model):
    name = models.CharField(max_length = 100)


class SwingerSignupDeclineReason(models.Model):
    name = models.CharField(max_length = 200)