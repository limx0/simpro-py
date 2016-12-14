
import unittest
import os; os.chdir('../..')
from simpropy.core import request_url
from simpropy.auth import UserTokenAuth, DirectAccessAuth

sandbox_host = 'sandbox.simpro.co'
sandbox_client_key = 'sandbox-simpro'
sandbox_client_secret = 'kQHjbVkKzPv0Y6-Oscwi2ORxBAev7PP-LjtTsH9Qv14K6TXqxPHXFOLaQoDmAjH0Kt48KRpeIFpcKcdBJA5z7Q'


class TestTokenAuth(unittest.TestCase):
    host = os.environ['SIMPROPY_HOST']
    client_key = os.environ['SIMPROPY_CLIENT_KEY']
    client_secret = os.environ['SIMPROPY_CLIENT_SECRET']
    auth = UserTokenAuth(host, client_key, client_secret)


class TestDirectAccess(unittest.TestCase):
    auth = DirectAccessAuth(sandbox_host, sandbox_client_key, sandbox_client_secret)

    def test_auth(self):
        payload = {"method": "CompanySearch", "jsonrpc": "2.0"}
        resp = self.auth.auth.post(request_url.format(sandbox_host), json=payload)
        self.assertTrue(resp.status_code == 200)

