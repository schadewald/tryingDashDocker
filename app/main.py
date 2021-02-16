from flask import Flask
api = Flask(__name__)


@api.route("/")
def hello():
    return "Hello World from Flask"
