# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lifestyleuser.models import LifestyleUser
from settingsandattributes.models import *

# Create your models here.

class Swinger(models.Model):
    user = models.ForeignKey(LifestyleUser, on_delete=models.CASCADE)
    swingertype = models.ForeignKey(SwingPreference, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    username = models.CharField(max_length=100, blank=True, null=True)
    sex1 = models.ForeignKey(SexType, related_name='swingersex1', on_delete=models.DO_NOTHING, blank=True, null=True)
    sex2 = models.ForeignKey(SexType, related_name='swingersex2', on_delete=models.DO_NOTHING, blank=True, null=True)
    orientation1 = models.ForeignKey(SexualOrientation, related_name='orientation1', on_delete=models.DO_NOTHING, blank=True, null=True)
    orientation2 = models.ForeignKey(SexualOrientation, related_name='orientation2', on_delete=models.DO_NOTHING, blank=True, null=True)
    birthday1 = models.DateField(blank=True, null=True)
    birthday2 = models.DateField(blank=True, null=True)
    ethnicity1 = models.ForeignKey(SwingerEthnicgroups, related_name='ethnicity1', on_delete=models.DO_NOTHING, blank=True, null=True)
    ethnicity2 = models.ForeignKey(SwingerEthnicgroups, related_name='ethnicity2', on_delete=models.DO_NOTHING, blank=True, null=True)
    verificationphoto = models.CharField(max_length=300, blank=True, null=True)
    verificationphotokey = models.CharField(max_length=300, blank=True, null=True)
    verificationphotocode = models.CharField(max_length=6, blank=True, null=True)
    bodytypeverificationphoto = models.CharField(max_length=300, blank=True, null=True)
    bodytypeverificationphotokey = models.CharField(max_length=300, blank=True, null=True)
    bodytypeverificationphotocode = models.CharField(max_length=6, blank=True, null=True)
    optinbodytypefiltering = models.BooleanField(default=False)
    allownonoptinbodytypeusers = models.BooleanField(default=False)
    bodytypesubmissiondate = models.DateField(blank=True, null=True)
    wantsinglewoman = models.BooleanField(default=False)
    wantsingleman = models.BooleanField(default=False)
    wantsinglets = models.BooleanField(default=False)
    wantcouplemanwoman = models.BooleanField(default=False)
    wantcouplewomanwoman = models.BooleanField(default=False)
    wantcouplewomants = models.BooleanField(default=False)
    wantcouplemanman = models.BooleanField(default=False)
    wantcouplemants = models.BooleanField(default=False)
    wantcoupletsts = models.BooleanField(default=False)
    wanthispanic = models.BooleanField(default=False)
    wantlatino = models.BooleanField(default=False)
    wantwhite = models.BooleanField(default=False)
    wantblack = models.BooleanField(default=False)
    wantasian = models.BooleanField(default=False)
    wantnativeamerican = models.BooleanField(default=False)
    wantpacificislander = models.BooleanField(default=False)
    minpreferedage = models.IntegerField(blank=True, null=True)
    maxpreferedage = models.IntegerField(blank=True, null=True)




