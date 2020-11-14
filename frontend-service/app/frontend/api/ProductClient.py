import requests

# host = 'product'
# host = 'debby-hand-knits.herokuapp.com'
# host = '0.0.0.0'
host = 'localhost'

class ProductClient:

    @staticmethod
    def get_product(slug):

        url = f'http://{host}:5000/product/' + slug

        response = requests.request(method="GET", url=url)

        response = requests.request(
            method="GET",
            url=f'http://{host}:5000/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get(f'http://{host}:5000/api/products')
        products = r.json()
        return products
