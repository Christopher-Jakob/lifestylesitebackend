from django.conf.urls import url, include
from views import LifeStyleUser, SwingerUserSignup, SwingerDeclineAcceptView
from hosts.urls import hosturls
from swingers.urls import swingerurls
from userauthenticationviews import UserGetSelf


userurls = [

    url('user/swinger/swingerdeclineaccept', SwingerDeclineAcceptView.as_view()),
    url('user/swinger', SwingerUserSignup.as_view()),
    url('user/login', UserGetSelf.as_view()),
    url('user', LifeStyleUser.as_view()),
    url('host/', include(hosturls)),
    url('swinger/',include(swingerurls))
]