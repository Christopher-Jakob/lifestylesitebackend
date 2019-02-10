from django.conf.urls import url, include
from countrystatecityviews import *
from hostypeviews import *
from swingertypeviews import *
from sextypeviews import *
from swingerethnictypes import *
from SwingerSignupDeclineReasonViews import *


countryurls = [
    url('countriesbystatus/(?P<status>([a-z]+))', GetActiveInactiveCountriesView.as_view()),
    url('makecountry', CreateCountryView.as_view()),
    url('countrydetail/(?P<pk>([0-9]+))', GetDeletePutCountryView.as_view())

]

stateandcityurls =[
    url('^stateandcitybystatus/(?P<type>([a-z]+))/(?P<relationpk>([0-9]+))/(?P<status>([a-z]+))$', GetActiveInactiveStatesCitiesView.as_view()),
    url('makestateorcity/(?P<type>([a-z]+))/(?P<pk>([0-9]+))', CreateStateCityView.as_view()),
    url('^stateorcitydetail/(?P<type>([a-z]+))/(?P<pk>([0-9]+))$', GetDeletePutStateCityView.as_view()),
    url('all/(?P<type>([a-z]+))',AllCountriesStatesCities.as_view())
]

hosttypeurls = [
    url('hosttypeallorcreate', GetAllCreateHostType.as_view()),
    url('hosttypedetail/(?P<pk>([0-9]+))', HostTypeGetPutDeleteView.as_view())
]

swingertypeurls = [
    url('swingtypeallorcreate',GetSwingerTypeGetAllCreate.as_view()),
    url('swingtypedetail/(?P<pk>([0-9]+))$', SwingerTypeDetailView.as_view())
]

sextypeurls = [
    url('sextypeallorcreate', PostGetAllSexTypes.as_view()),
    url('sextypedetail/(?P<pk>([0-9]+))', SexTypeDetail.as_view())
]

swingerethnictypes = [
    url('ethnictypeallorcreate', PostGetallSwingerEthnictypes.as_view()),
    url('ethnictypedetail/(?P<pk>([0-9]+))', SwingerEthnictypedetail.as_view())
]

swingersignupdeclinereasons = [
    url('swingersignupdeclinereason/(?P<pk>([0-9]+))', DeleteSwingerSignupDeclineReasonView),
    url('swingersignupdeclinereason', SwingerSignupDeclineReasonView.as_view()),

]

settingsandattributesurls = [
    url('country/',include(countryurls)),
    url('stateandcity/',include(stateandcityurls)),
    url('hosttype/', include(hosttypeurls)),
    url('swingertype/', include(swingertypeurls)),
    url('sextype/',include(sextypeurls)),
    url('ethnictype/',include(swingerethnictypes)),
    url('swingerdeclinereason/', include(swingersignupdeclinereasons))

]
