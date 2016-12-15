# simpro-py
A python wrapper for the SimPro API - http://api.simpro.co/


### Installation
```python
>>> pip install simpropy
```

### Quick-start

```python
>>> simpro = SimPro(hostname, client_key, client_secret)
>>> simpro.customers.search_by_name('Apple')
[{'CustomerID': 4967, 'FirstName': 'Apple Computers', ... }]
```