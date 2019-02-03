from django.conf.urls import url
from swingers.views import GetAllSwingers

swingerurls = [
    url('all',GetAllSwingers.as_view())
]