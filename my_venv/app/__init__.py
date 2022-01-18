from flask import Flask
from .models import db

app = Flask(__name__)

from app import routes
from app import models

# initialize database
db.init_app(app)

from . import routes
from . import models














