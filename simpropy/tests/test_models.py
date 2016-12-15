
from simpropy.tests.test_core import TestSimPro


class TestModels(TestSimPro):
    def test_customer(self):
        customers = self.sim_pro.customer.search_by_name('%')
        self.assertTrue(customers)