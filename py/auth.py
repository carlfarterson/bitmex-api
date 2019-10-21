import time
import urllib
import json
import hmac
import requests as r
from hashlib import sha256
from datetime import datetime, timedelta, timezone


class Auth:

    def __init__(self, api_key, api_secret, test):
        self.path = '/api/v1/'
        self.api_secret = api_secret
        self.headers = {'api-key': api_key,
                        'api-expires': None,
                        'api-signature': None}

        if test:
            self.base_url = 'https://testnet.bitmex.com'
        else:
            self.base_url = 'https://bitmex.com'

    def _create_path(self, action, **param):
        path = self.path + action
        if param:
            path += '?' + urllib.parse.urlencode(param)
        return path

    def _update_headers(self, method, path):
        ''' Update the data included in the header of our API call. '''
        self._update_expiration()
        self._update_signature(method, path)

    def _update_expiration(self):
        ''' Timestamp after which request is invalid to prevent replay attacks. '''
        expires = str(int(round(time.time()) + 5))   # 5 second window to execute trade
        self.headers['api-expires'] = expires

    def _update_signature(self, method, path):
        msg = method + path + self.headers['api-expires']
        self.headers['api-signature'] = hmac.new(bytes(self.api_secret, 'utf8'),
                                                 bytes(msg, 'utf8'),
                                                 digestmod=sha256).hexdigest()

    def _send_request(self, method, path):
        response = getattr(r, method.lower())(self.base_url+path, headers=self.headers).json()
        return response
