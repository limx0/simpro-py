
from simpropy.auth import UserTokenAuth
from simpropy.definitions import Customer

request_url = 'https://{}/api/index.php'


class SimPro:
    def __init__(self, host, client_key, client_secret, auth_type='user_token', company_id=0, auth_file=''):
        self.host = host
        self.company_id = company_id
        if auth_type == 'user_token':
            self.auth = UserTokenAuth(host, client_key, client_secret, auth_file=auth_file)
        self.customer = Customer(self)

    def request(self, end_point, parameters=None):
        if parameters is None:
            parameters = {}
        parameters.update({'CompanyID': self.company_id})
        payload = {
            "method": end_point,
            "params": parameters,
            "jsonrpc": "2.0",
        }
        json_resp = self.auth.auth.post(request_url.format(self.host), json=payload).json()
        if json_resp['error'] is not None:
            raise Exception(json_resp['error']['faultString'])
        return json_resp