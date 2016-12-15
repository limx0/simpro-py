
class Base(object):
    def __init__(self, parent):
        self.request = parent.request
        self.company_id = parent.company_id
        self.class_name = self.__class__.__name__

    def search_by_name(self, search, limit=500):
        return self.request(
            end_point='{cls}Search'.format(cls=self.class_name),
            parameters={'CompanyID': self.company_id, 'Search': search, 'Limit': limit}
        )

    def search_by_fields(self, field_value_dict, limit=500):
        return self.request(
            end_point='{cls}SearchFields'.format(cls=self.class_name),
            parameters={'CompanyID': self.company_id, 'SearchTerms': field_value_dict, 'Limit': limit}
        )

    def insert(self, parameters):
        return self.request(
            end_point='{}Insert'.format(self.class_name),
            parameters={'CompanyID': self.company_id, '{}Details'.format(self.name.title()): parameters}
        )

    def update(self, id, details):
        return self.request(
            end_point='{cls}Update'.format(cls=self.class_name),
            parameters={
                'CompanyID': self.company_id,
                self.id: id,
                '{}Details'.format(self.name.title()): details}
        )


class Customer(Base):
    name = 'customer'
    id = 'CustomerID'

    def __init__(self, parent):
        super().__init__(parent)


class Job(Base):
    name = 'job'
    id = 'JobNo'

    def __init__(self, parent):
        super().__init__(parent)


class Site(Base):
    name = 'site'
    id = 'SiteNo'

    def __init__(self, parent):
        super().__init__(parent)


class Employee(Base):
    name = 'employee'
    id = 'EmployeeID'

    def __init__(self, parent):
        super().__init__(parent)


class CustomerInvoice(Base):
    name = 'customer_invoice'
    detail = 'invoice'

    def __init__(self, parent):
        super().__init__(parent)
