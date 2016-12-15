
import unittest
import os
os.chdir('../..')
from simpropy.core import request_url
from simpropy.auth import UserTokenAuth, DirectAccessAuth


sandbox_host = 'sandbox.simpro.co'
sandbox_client_key = 'sandbox-simpro'
sandbox_client_secret = 'kQHjbVkKzPv0Y6-Oscwi2ORxBAev7PP-LjtTsH9Qv14K6TXqxPHXFOLaQoDmAjH0Kt48KRpeIFpcKcdBJA5z7Q'


def sample_request(auth, host):
    payload = {"method": "CompanySearch", "parameters": [], "jsonrpc": "2.0", "CompanyID": 0}
    return auth.auth.post(request_url.format(host), json=payload)


class TestTokenAuth(unittest.TestCase):
    def test_auth(self):
        host = os.environ['SIMPROPY_HOST']
        client_key = os.environ['SIMPROPY_CLIENT_KEY_USER']
        client_secret = os.environ['SIMPROPY_CLIENT_SECRET_USER']
        auth = UserTokenAuth(host, client_key, client_secret)
        resp = sample_request(auth, host)
        self.assertTrue(resp.status_code == 200)


class TestDirectAccess(unittest.TestCase):
    def test_auth(self):
        auth = DirectAccessAuth(sandbox_host, sandbox_client_key, sandbox_client_secret)
        resp = sample_request(auth, sandbox_host)
        self.assertTrue(resp.status_code == 200)
