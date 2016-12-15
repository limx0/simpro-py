
import os
import unittest
from simpropy.core import SimPro


class TestSimPro(unittest.TestCase):
    host = os.environ['SIMPROPY_HOST']
    client_key = os.environ['SIMPROPY_CLIENT_KEY']
    client_secret = os.environ['SIMPROPY_CLIENT_SECRET']
    sim_pro = SimPro(host, client_key, client_secret)

    def test_request(self):
        self.assertTrue(self.sim_pro.request('CompanySearch'))
