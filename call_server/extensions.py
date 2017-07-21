# define flask extensions in separate file, to resolve import dependencies

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_caching import Cache
cache = Cache()

from flask_assets import Environment
assets = Environment()

from flask_babel import Babel
babel = Babel()

from flask_mail import Mail
mail = Mail()

from flask_login import LoginManager
login_manager = LoginManager()

from flask_restless import APIManager
rest = APIManager()

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

from flask_store import Store
store = Store()

from flask_rq2 import RQ
rq = RQ()

from flask_talisman import Talisman
CALLPOWER_CSP = {
    'default-src':'\'self\'',
    'script-src':['\'self\'', '\'unsafe-inline\'', 'cdnjs.cloudflare.com'],
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'fonts.googleapis.com'], 
    'font-src': ['\'self\'', 'fonts.gstatic.com']
}
talisman = Talisman()