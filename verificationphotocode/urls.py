from django.conf.urls import url
from views import *

verificationphotourls = [
    url('code/(?P<pk>([0-9]+))/(?P<code>([0-9]+))', VerificationPhotoCodeview.as_view()),
    url('code', VerificationPhotoCodeview.as_view())

]