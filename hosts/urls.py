from django.conf.urls import url
from views import *

hosturls = [
    url('all', GetAllHosts.as_view())
]