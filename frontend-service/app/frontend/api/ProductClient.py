import requests

# host = 'product'
host = 'basic-django.herokuapp.com'
# host = '0.0.0.0:5000'
# host = 'localhost'


class ProductClient:

    @staticmethod
    def get_product(slug):

        url = f'http://{host}/product/' + slug
        print(url)

        response = requests.request(method="GET", url=url)

        response = requests.request(
            method="GET",
            url=f'http://{host}/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get(f'http://{host}/api/products')
        products = r.json()
        return products
