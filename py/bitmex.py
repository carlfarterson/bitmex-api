import urllib
import json
import hashlib
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


    def trade(self, symbol='XBTUSD'):

        # Create message
        query = urllib.parse.urlencode({'symbol': symbol})
        path = self.path + 'trade?' + query
        message = self.create_message(request='GET', path)
        # Create signature
        self.create_signature(request='GET', action='trade', symbol=symbol)
        # Send request
        self.send_request()


    def create_signature(self, request, action, **query):
        query = urllib.parse.urlencode(query)
        path = self.path + action + '?' + query

        self.update_headers(request, path)
        self.send_request(path)


    def update_headers(self, request, path):
        api_expires = self.api_expires()
        msg = request + path + api_expires
        signature = hmac.new(bytes(self.api_secret, 'utf8'), bytes(message, 'utf8'), digestmod=hashlib.sha256).hexdigest()
        self.headers['api-signature'] = signature


    def send_request(self, path):
        response = requests.get(self.url + path, headers=self.headers).json()
        return response


    def api_expires(self, seconds=15):
        ''' UNIX timestamp after which the request is no longer valid.
        This prevents replay attacks.
        '''
        end_timestamp = (datetime.utcnow() + timedelta(seconds=seconds)).timestamp()
        self.headers['api-expires'] = str(int(end_timestamp))
        return self.headers['api-expires']






# query = {'symbol': 'XBTUSD',
#          'startTime': (datetime.utcnow() - timedelta(seconds=30)).isoformat(timespec='seconds')}



path = '/api/v1/trade?'+ query
msg = 'GET' + path + expires
url = 'https://testnet.bitmex.com' + path




api = {
    'api-expires': expires,
    'api-key': ID_test,
    'api-signature': signature
}
