from flask import session
import requests
# user = action

# host = 'user'
# host = 'debby-hand-knits.herokuapp.com'
host = '0.0.0.0:5000'
# host = 'localhost'

class UserClient:

    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }

        url = f'http://{host}/api/user'
        print(url)

        response = requests.request(
            method="GET", url=url, headers=headers)

        if response.status_code == 401:
            return False

        user = response.json()
        return user
