from lifestylesite.settings import EMAILAPIBASEURL, EMAILAPIKEY, EMAILADDRESS
import requests
from django.template.loader import render_to_string

def sendemail(template, email):
    template = render_to_string(template)
    return requests.post(
        EMAILAPIBASEURL,
        auth=("api",EMAILAPIKEY),
        data={'from': EMAILADDRESS,
              'to': [email],
              'subject': 'Test Email',
              'html': template
              }

    )



