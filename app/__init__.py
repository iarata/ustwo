from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.assets import Environment, Bundle

app = Flask(__name__, static_folder='static', static_url_path='')

# Load config.
app.config.from_object('config')

# Setup the database.
db = MongoEngine(app)

# Assets
assets = Environment()
css = Bundle('css/index.sass', filters='sass', depends=['css/**/*.sass', 'css/**/**/*.sass'], output='css/index.css')
assets.register('css_all', css)
assets.init_app(app)

# So we can use Jade templates.
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# Register blueprints
from app import routes
app.register_blueprint(routes.clones.bp)

from app import logging
