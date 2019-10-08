from py.config import *
from py.auth import Auth


class Bitmex(Auth):

    def __init__(self, api_key, api_secret, test=True):
        super().__init__(api_key, api_secret, test)

    def trade(self, **param):
        # b.trade(symbol='XBTUSD', startTime=(datetime.utcnow() - timedelta(seconds=10)).isoformat(timespec='seconds'))
        return self.run(action='trade', **param)

    def order(self, **param):
        # b.order(method='POST', symbol='XBTUSD', orderType='StopLimit', orderQty=1, price=8500, stop_px=8450)
        return self.run(action='order', **param)

    def run(self, action, method='GET', **param):
        path = self._create_path(action, **param)
        self._update_headers(method, path)
        response = self._send_request(method, path)
        return response


# b = Bitmex(api_key=api_key_test, api_secret=api_secret_test)
#
# results = b.order()[::-1]
# btc = list(filter(lambda x: x['symbol'] == 'XBTUSD', results))
#
# for i in range(len(btc)):
#     for x in ['orderID', 'clOrdID', 'clOrdLinkID', 'account', 'multiLegReportingType', 'text']:
#         btc[i].pop(x)
#
# btc[0]
