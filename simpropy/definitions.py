
class Customer:
    def __init__(self, parent):
        self.request = parent.request
        self.company_id = parent.company_id

    def customer_insert(self, title, first_name, last_name):
        args = {'CustomerType': 'Customer', 'Title': title, 'FirstName': first_name, 'LastName': last_name}
        return self.request(end_point='CustomerInsert', parameters={'CustomerDetails': args, 'CompanyID': self.company_id})

    def customer_search(self):
        return self.request(end_point='CustomerSearch', parameters={'CompanyID': self.company_id})