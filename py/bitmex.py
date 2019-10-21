from py.config import *
from py.auth import Auth
import time


class Bitmex(Auth):

    def __init__(self, api_key=None, api_secret=None, test=True):
        super().__init__(api_key, api_secret, test)

    def trade(self, **param):
        return self.run(action='trade', **param)
        # example:  b.trade(symbol='XBTUSD', startTime=int(round(time.time()) - 15))

    def order(self, **param):
        return self.run(action='order', **param)
        # example:  b.order(method='POST', symbol='XBTUSD', orderType='StopLimit', orderQty=1, price=8500, stop_px=8450)

    def run(self, action, method='GET', **param):
        path = self._create_path(action, **param)
        self._update_headers(method, path)
        response = self._send_request(method, path)
        return response
