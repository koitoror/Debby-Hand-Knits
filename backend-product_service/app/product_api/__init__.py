from flask import Blueprint

# product_api_blueprint = Blueprint('product_api', __name__)
product_api_blueprint = Blueprint('product_api', __name__,  url_prefix='/products')


from . import routes