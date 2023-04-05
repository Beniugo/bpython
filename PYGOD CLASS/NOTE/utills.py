import requests
from pprint import pprint
base_url = 'https://fakestoreapi.com'
endpoints = {
    'products': '/products',
    'categories': '/products/categories'
}

def get_products():
    url = base_url + endpoints['products']
    return requests.get(url =url).json()[:11]

def get_categories():
    url = base_url + endpoints['categories']
    return requests.get(url=url).json()

if __name__ == '__main__':
    get_categories()
#pprint(get_categories())
#pprint(get_products())


