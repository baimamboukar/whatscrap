from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return "<p>This is a simple Flask app.</p>"


@app.route("/contact")
def contact():
    return "<p>Contact us here....</p>"
