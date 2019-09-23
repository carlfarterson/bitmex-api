import urllib
import json
from hashlib import sha256
import hmac
import requests
from datetime import datetime, timedelta, timezone
from py.config import *


class Bitmex:

    def __init__(self, api_key, api_secret, test=True):
        self.path = '/api/v1/'
        self.api_secret = api_secret
        self.headers = {'api-expires': '',
                        'api-key': api_key,
                        'api-signature': ''}

        if test:
            self.url = 'https://testnet.bitmex.com'
        else:
            self.url = 'https://bitmex.com'


    def trade(self, **param):
        return self.run(request='GET', action='trade', **param)


    def run(self, request='GET', action='trade', **param):
        path = self._create_path(action, **param)
        self._update_headers(request, path)
        response = self._send_request(path)
        return response


    def _create_path(self, action, **param):
        path = self.path + action
        if param:
            path += '?' + urllib.parse.urlencode(param)
        return path


    def _update_headers(self, request, path):
        ''' Update the data included in the header of our API call. '''
        self._update_expiration()
        self._update_signature(request, path)


    def _update_expiration(self):
        ''' Timestamp after which request is invalid to prevent replay attacks. '''
        end_timestamp = (datetime.utcnow() + timedelta(seconds=15)).timestamp()
        self.headers['api-expires'] = str(int(end_timestamp))


    def _update_signature(self, request, path):
        msg = request + path + self.headers['api-expires']
        self.headers['api-signature'] = hmac.new(bytes(self.api_secret, 'utf8'),
                                                 bytes(msg, 'utf8'),
                                                 digestmod=sha256).hexdigest()


    def _send_request(self, path):
        response = requests.get(self.url + path, headers=self.headers).json()
        return response

        # query = {'symbol': 'XBTUSD',
        #          'startTime': (datetime.utcnow() - timedelta(seconds=30)).isoformat(timespec='seconds')}


b = Bitmex(api_key=api_key_test, api_secret=api_secret_test)
b.trade(symbol='XBTUSD', startTime=(datetime.utcnow() - timedelta(seconds=10)).isoformat(timespec='seconds'))
