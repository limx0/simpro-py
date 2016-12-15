
import unittest
from simpropy.core import SimPro
from simpropy.tests.test_auth import sandbox_host, sandbox_client_key, sandbox_client_secret


class TestSimProSandbox(unittest.TestCase):
    simpro = SimPro(sandbox_host, sandbox_client_key, sandbox_client_secret, company_id=2)


class TestCustomer(TestSimProSandbox):
    def test_insert(self):
        self.assertTrue(self.simpro.customer.insert({'FirstName': 'Test'}))

    def test_update(self):
        self.assertTrue(self.simpro.customer.update(id=13676, details={'FirstName': 'Test'}))

    def test_search_by_name(self):
        self.assertTrue(self.simpro.customer.search_by_name('%'))

    def test_search_by_fields(self):
        self.assertTrue(self.simpro.customer.insert({'FirstName': 'Test'}))


class TestSite(TestSimProSandbox):
    def test_search_by_name(self):
        self.assertTrue(self.simpro.site.search_by_name('%'))


class TestJob(TestSimProSandbox):
    def test_insert(self):
        self.assertTrue(self.simpro.job.insert({'CustomerID': 13676, 'SiteID': 24280}))

    def test_update(self):
        self.assertTrue(self.simpro.job.update(id=5162, details={'Description': 'Hello'}))

    def test_search_by_name(self):
        self.assertTrue(self.simpro.job.search_by_name('%'))

    def test_search_by_fields(self):
        self.assertTrue(self.simpro.job.insert({'CustomerID': 13676, 'SiteID': 24280, 'Description': 'Test'}))
