
class Customer:
    def __init__(self, parent):
        self.parent = parent

    def customer_insert(self, Title, FirstName, LastName):
        details = {'CustomerType': 'Customer', 'Title': Title, 'FirstName': FirstName, 'LastName': LastName}
        return self.parent.request(end_point='CustomerInsert', parameters={'CustomerDetails': details})
