import requests
from settingsandattributes.models import Country, State, City
from lifestylesite.settings import BASEGEOLOCATIONAPIURL , GEOLOCATIONAPIKEY


def getlatlongcountry(countrypk):
    instance = Country.objects.get(pk=countrypk)
    name = instance.name
    url = BASEGEOLOCATIONAPIURL + name + '&key=' + GEOLOCATIONAPIKEY
    r = requests.get(url).json()
    r = r['results'][0]['geometry']['location']
    dic = {
        "lat": r['lat'],
        "long": r['lng']
    }
    return dic


def getlatlongstate(statepk):
    instance = State.objects.get(pk=statepk)
    statename = instance.name
    countryname = instance.country.name
    name = countryname + ' ' + statename
    url = BASEGEOLOCATIONAPIURL + name + '&key=' + GEOLOCATIONAPIKEY
    r = requests.get(url).json()
    r = r['results'][0]['geometry']['location']
    dic = {
        "lat": r['lat'],
        "long": r['lng']
    }
    return dic


def getlatlongcity(citypk):
    instance = City.objects.get(pk=citypk)
    cityname = instance.name
    stateinstance = instance.state
    statename = instance.state.name
    countryname = stateinstance.country.name
    name = countryname + ' ' + statename + ' ' + cityname
    url = BASEGEOLOCATIONAPIURL + name + '&key=' + GEOLOCATIONAPIKEY
    r = requests.get(url).json()
    r = r['results'][0]['geometry']['location']
    dic = {
        "lat": r['lat'],
        'long': r['lng']
    }
    return dic


def setalllatlong():
    countries = Country.objects.all()
    for country in countries:
        pk = country.pk
        coordinates = getlatlongcountry(pk)
        country.lat = coordinates['lat']
        country.long = coordinates['long']
        country.save()
    states = State.objects.all()
    for state in states:
        pk = state.pk
        coordinates = getlatlongstate(pk)
        state.lat = coordinates['lat']
        state.long = coordinates['long']
        state.save()
    cities = City.objects.all()
    for city in cities:
        pk = city.pk
        coordinates = getlatlongcity(pk)
        city.lat = coordinates['lat']
        city.long = coordinates['long']
        city.save()

