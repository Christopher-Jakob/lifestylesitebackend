# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extraarguments):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),
                           **extraarguments)
        if not password:
            user.set_unusable_password()
            user.save()
            return user

        user.set_pasword(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email,  password=None, **extraarguments):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),
                           **extraarguments)

        if not password:
            user.set_unusable_password()
            user.save()
            return user

        user.set_pasword(password)
        user.is_active = True
        user.save()
        return user


class LifestyleUser(AbstractBaseUser):
    email = models.EmailField(unique = True)
    is_active = models.BooleanField(default=False)
    isadmin = models.BooleanField(default=False)
    isswingerapproved = models.BooleanField(default=False)
    ishostapproved = models.BooleanField(default=False)
    isswinger = models.BooleanField(default = False)
    ishost = models.BooleanField(default=False)
    prelaunchsignup = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_long_name(self):
        return self.email


