import urllib
import json
import hashlib
import hmac
import requests
from datetime import datetime, timedelta, timezone
from py.config import *


class Bitmex:

    def __init__(self, api_key, api_secret, test=True):
        self.api_secret = api_secret
        self.headers = {'api-expires': '',
                        'api-key': api_key,
                        'api-signature': ''}

        if test:
            self.url = 'https://testnet.bitmex.com'
        else:
            self.url = 'https://bitmex.com'


    def api_expires(self, seconds=15):
        ''' UNIX timestamp after which the request is no longer valid.
        This prevents replay attacks.
        '''
        end_timestamp = (datetime.utcnow() + timedelta(seconds=seconds)).timestamp()
        end_timestamp_str = str(int(end_timestamp))
        return end_timestamp_str


    def do_something():
        # Create signature
        create_signature()
        # Send request
        send_request()


    def signature(self):
        sig_hash











query = {
    'symbol': 'XBTUSD',
    'startTime': (datetime.utcnow() - timedelta(seconds=30)).isoformat(timespec='seconds')
}

query = urllib.parse.urlencode(query)

expires = str(int((datetime.utcnow() + timedelta(seconds=15)).timestamp()))

path = '/api/v1/trade?'+ query
msg = 'GET' + path + expires
url = 'https://testnet.bitmex.com' + path


signature = hmac.new(bytes(Secret_test, 'utf8'), bytes(msg, 'utf8'), digestmod=hashlib.sha256).hexdigest()

api = {
    'api-expires': expires,
    'api-key': ID_test,
    'api-signature': signature
}



requests.get(url, headers=api).json()
