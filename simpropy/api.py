
from simpropy.auth import UserTokenAuth

request_url = 'https://{}/api/index.php'


class SimPro:
    def __init__(self, host, client_key, client_secret, auth_type='user_token', company_id=0):
        self.host = host
        self.company_id = company_id
        if auth_type == 'user_token':
            self.auth = UserTokenAuth(host, client_key, client_secret, cache_auth=True).auth

    def customer_search(self):
        return self.request(end_point='CustomerSearch')

    def request(self, end_point):
        payload = {
            "method": end_point,
            "params": {'CompanyID': self.company_id},
            "jsonrpc": "2.0",
        }
        json_resp = self.auth.post(request_url.format(self.host), json=payload).json()
        if json_resp['error'] is not None:
            raise Exception(json_resp['error'])
        return json_resp['result']

