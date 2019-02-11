from django.conf.urls import url
from swingers.views import GetAllSwingers
from swingersignupapprovaldenialviews import SwingerApprovalListGet

swingerurls = [
    url('all',GetAllSwingers.as_view()),
    url('swingerapplicationlist', SwingerApprovalListGet.as_view())
]