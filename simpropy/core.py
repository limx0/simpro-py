
from simpropy.auth import DirectAccessAuth, UserTokenAuth
from simpropy.definitions import Base

request_url = 'https://{}/api/index.php'


class SimPro:
    def __init__(self, host, client_key, client_secret, auth_type='direct_access', company_id=0):
        self.host = host
        self.company_id = company_id
        if auth_type == 'direct_access':
            self.auth = DirectAccessAuth(host, client_key, client_secret)
        elif auth_type == 'user_token':
            self.auth = UserTokenAuth(host, client_key, client_secret)
        else:
            raise Exception('auth_type {} not understood. Should be [direct_access, user_token]'.format(auth_type))

        for cls in Base.__subclasses__():
            setattr(self, cls.name, cls(self))

    def _request(self, end_point, parameters=None):
        if parameters is None:
            parameters = {'CompanyID': 0}
        payload = {
            "method": end_point,
            "params": parameters,
            "jsonrpc": "2.0",
        }
        json_resp = self.auth.auth.post(request_url.format(self.host), json=payload).json()
        if json_resp['error'] is not None:
            raise Exception(json_resp['error']['faultString'])
        return json_resp['result']
