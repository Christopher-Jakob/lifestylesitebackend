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
    birthday1 = models.DateField(blank=True, null=True)
    birthday2 = models.DateField(blank=True, null=True)
    ethnicity1 = models.ForeignKey(SwingerEthnicgroups, related_name='ethnicity1', on_delete=models.DO_NOTHING, blank=True, null=True)
    ethnicity2 = models.ForeignKey(SwingerEthnicgroups, related_name='ethnicity2', on_delete=models.DO_NOTHING, blank=True, null=True)
    verificationphoto = models.CharField(max_length=300, blank=True, null=True)
    verificationphotokey = models.CharField(max_length=300, blank=True, null=True)
    verificationphotocode = models.CharField(max_length=6, blank=True, null=True)




