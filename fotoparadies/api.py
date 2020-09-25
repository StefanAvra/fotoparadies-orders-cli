import requests

URL = ''
with open('api_endpoint.txt') as f:
    URL = f.readline()

def get_order_info(shop, order):
    p = {'config':1320, 'shop': shop, 'order': order}
    r = requests.get(URL, params=p)
    return r.json()

def get_order_status(shop, order):
    return get_order_info(shop, order)['summaryStateCode']