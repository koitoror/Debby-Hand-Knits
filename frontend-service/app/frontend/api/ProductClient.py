import requests


class ProductClient:

    @staticmethod
    def get_product(slug):

        # host = 'product'
        host = 'debby-hand-knits.herokuapp.com'
        url = f'{host}:5000/product/' + slug

        response = requests.request(method="GET", url=url)


        response = requests.request(method="GET", url='http://product:5000/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get('http://product:5000/api/products')
        products = r.json()
        return products
