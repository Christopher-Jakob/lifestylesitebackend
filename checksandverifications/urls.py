from django.conf.urls import url, include
from views import EmailNotTaken, VerifyPassword

checksandverificationurls = [
    url('email',EmailNotTaken.as_view()),
    url('password/(?P<pk>([0-9]+))',VerifyPassword.as_view())

]