from flask import Flask

app = Flask(__name__)

from app.controllers import (routes, pwa)

app.register_blueprint(routes.stefnotes)
app.register_blueprint(pwa.stefnotes)
