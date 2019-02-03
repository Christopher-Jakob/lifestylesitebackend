import requests
from lifestylesite.settings import EMAILPUBLICVALIDATIONKEY



def validateemail(emailaddress):
    return requests.get(
        "https://api.mailgun.net/v3/address/validate",
        auth=("api", EMAILPUBLICVALIDATIONKEY ),
        params={'address': emailaddress}
    )

