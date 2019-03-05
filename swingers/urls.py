from django.conf.urls import url
from swingers.views import GetAllSwingers, ModifySwinger
from swingersignupapprovaldenialviews import SwingerApprovalListGet, SwingerBodyTypeClassificationListGet


swingerurls = [
    url('all',GetAllSwingers.as_view()),
    url('swingerapplicationlist', SwingerApprovalListGet.as_view()),
    url('swingerbodytypeapplicationlist', SwingerBodyTypeClassificationListGet.as_view() ),
    url('swingerdetail/(?P<pk>([0-9]+))',ModifySwinger.as_view())
]