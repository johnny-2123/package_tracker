from flask import Flask, render_template, Blueprint
from flask_migrate import Migrate
from .config import Configuration
from .routes import index
from .models import db

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(index.bp)
db.init_app(app)
migrate = Migrate(app, db)
