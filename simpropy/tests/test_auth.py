
import unittest
import os
from simpropy.api import SimPro
from simpropy.auth import UserTokenAuth


host = os.environ['SIMPROPY_HOST']
client_key = os.environ['SIMPROPY_KEY']
client_secret = os.environ['SIMPROPY_SECRET']


class TestAuth(unittest.TestCase):
    auth = UserTokenAuth(host, client_key, client_secret, cache_auth=True)


class TestSimPro(TestAuth):

    sim_pro = SimPro(host, client_key, client_secret)

    def test_request(self):
        self.assertTrue(self.sim_pro.request('CustomerSearch'))

    def test_customer_search(self):
        self.assertTrue(self.sim_pro.customer_search())
