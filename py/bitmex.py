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


    def trade(self, symbol='XBTUSD'):
        return self.run(request='GET', action='trade', symbol=symbol)


    def run(self, request='GET', action='trade', **param):

        path = self.create_path(action, param)
        self.update_headers(request, path)
        response = self.send_request(path)
        return response

    def create_path(action, **param):
        path = self.path + action
        if param:
            path += '?' + urllib.parse.urlencode(param)
        return path


    def update_headers(self, request, path):
        ''' Update the data included in the header of our API call. '''
        self.update_expiration()
        msg = request + path + self.headers['api-expires']
        signature = hmac.new(bytes(self.api_secret, 'utf8'), bytes(message, 'utf8'), digestmod=sha256).hexdigest()
        self.headers['api-signature'] = signature


    def update_expiration(self):
        ''' Timestamp after which request is invalid to prevent replay attacks. '''
        end_timestamp = (datetime.utcnow() + timedelta(seconds=15)).timestamp()
        self.headers['api-expires'] = str(int(end_timestamp))


    def send_request(self, path):
        response = requests.get(self.url + path, headers=self.headers).json()
        return response





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
