
from simpropy.auth import authorize
from simpropy.models import Base

request_url = 'https://{}/api/index.php'


class SimPro:
    def __init__(self, host, client_key, client_secret, auth_type='direct_access', company_id=0):
        self.host = host
        self.company_id = company_id
        self.auth = authorize(auth_type, host, client_key, client_secret)
        for cls in Base.__subclasses__():
            setattr(self, cls.name, cls(self))

    def request(self, end_point, parameters=None):
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
