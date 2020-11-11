from flask import session
import requests


class OrderClient:

    @staticmethod
    def get_order():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }

        # host = 'order'
        host = 'debby-hand-knits.herokuapp.com'
        url = f'{host}:5000/api/order'

        response = requests.request(method="GET", url=url, headers=headers)

        order = response.json()
        return order

    @staticmethod
    def update_order(items):

        # host = 'order'
        host = 'debby-hand-knits.herokuapp.com'
        url = f'http://{host}:5000/api/order/update'

        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data=items, headers=headers)
        if response:
            order = response.json()

            return order

    @staticmethod
    def post_add_to_cart(product_id, qty=1):
        payload = {
            'product_id': product_id,
            'qty': qty,
        }

        # host = 'order'
        host = 'debby-hand-knits.herokuapp.com'
        url = f'http://{host}:5000/api/order/add-item'

        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data=payload, headers=headers)
        if response:
            order = response.json()

            return order

    @staticmethod
    def post_checkout():

        # host = 'order'
        host = 'debby-hand-knits.herokuapp.com'
        url = f'http://{host}:5000/api/order/checkout'
        
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data={}, headers=headers)
        order = response.json()
        return order

    @staticmethod
    def get_order_from_session():
        default_order = {
            'items': {},
            'total': 0,
        }
        return session.get('order', default_order)


