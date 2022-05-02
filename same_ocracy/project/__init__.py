from flask import Flask

app = Flask(__name__)

from project.home.views import home_blueprint

app.register_blueprint(home_blueprint)
