from maclookup import ApiClient
import logging

client = ApiClient('at_gVL2VUlnXzRjD9mkj70Avd6bqgdkm')

logging.basicConfig(filename='myapp.log', level=logging.WARNING)

print(client.get_raw_data('00A043AAAAAA', 'json'))
print(client.get_vendor('BBA043AAAAAA'))
print(client.get('BBA043AAAAAA'))

response = client.get('00A043AAAAAA')
print(response.vendor_details.is_private)
print(response.block_details.date_created)