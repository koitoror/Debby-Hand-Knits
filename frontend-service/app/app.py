from flask import Blueprint, Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from frontend import frontend_blueprint
import os

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'main.login'

bootstrap = Bootstrap(app)

# host = 'localhost'
host = 'degem-products.herokuapp.com'
# host = '0.0.0.0:5000'
# host = 'localhost'

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key",
    PRODUCT_SERVICE=f'http://{host}',
    # PRODUCT_SERVICE=f'http://{host}:8081'
))

app.register_blueprint(frontend_blueprint)

port = int(os.environ.get("PORT", 5000))

app.run(debug=True, host='0.0.0.0', port=port)
