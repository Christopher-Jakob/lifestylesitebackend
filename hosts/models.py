# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lifestyleuser.models import LifestyleUser
from settingsandattributes.models import *

# Create your models here.

class Hosts(models.Model):
    user = models.ForeignKey(LifestyleUser, on_delete =models.CASCADE)
    hosttype = models.ForeignKey(HostTypes, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

