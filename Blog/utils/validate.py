import requests
import os
from ..models import Entry, Feature
from datetime import datetime

RECAPTCHA_SECRET = os.environ.get('RECAPTCHA_SECRET')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def valid_recaptcha(request, captcha_rs):
    if request.method == 'POST':
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': RECAPTCHA_SECRET,
            'response': captcha_rs,
            'remoteip': get_client_ip(request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()

        status = verify_rs.get("success", False)

        return status
