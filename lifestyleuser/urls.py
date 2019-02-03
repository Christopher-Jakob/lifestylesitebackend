from django.conf.urls import url, include
from views import LifeStyleUser, SwingerUserSignup
from hosts.urls import hosturls
from swingers.urls import swingerurls


userurls = [
    url('^user/swinger$', SwingerUserSignup.as_view()),
    url('user', LifeStyleUser.as_view()),
    url('host/', include(hosturls)),
    url('swinger/',include(swingerurls))
]