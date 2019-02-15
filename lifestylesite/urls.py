"""lifestylesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from settingsandattributes.urls import settingsandattributesurls
from lifestyleuser.urls import userurls
from aws.urls import awsurls
from passwordvalidateview import PasswordValidate
from verificationphotocode.urls import verificationphotourls





siteadminurls = [
    url('settings/', include(settingsandattributesurls)),
    url('passwordvalidate', PasswordValidate.as_view()),
]

rootapiurls = [
    url('siteadmin/', include(siteadminurls)),
    url('user/', include(userurls)),
    url('aws/',include(awsurls)),
    url('verificationphoto/', include(verificationphotourls))
]


urlpatterns = [
    url('api/',include(rootapiurls)),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),


]
