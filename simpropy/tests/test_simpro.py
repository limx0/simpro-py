

from simpropy.core import SimPro
from simpropy.tests.test_auth import TestDirectAccess, sandbox_host, sandbox_client_key, sandbox_client_secret


class TestSimPro(TestDirectAccess):

    sim_pro = SimPro(sandbox_host, sandbox_client_key, sandbox_client_secret, company_id=2)

    def test_request(self):
        self.assertTrue(self.sim_pro.request('CompanySearch'))

    def test_customer_insert(self):
        resp = self.sim_pro.customer.customer_insert('Mr', 'Steve', 'Jobs')
        self.assertTrue(resp['result'])

    def test_customer_search(self):
        resp = self.sim_pro.customer.customer_search()
        self.assertTrue(resp['result'])

