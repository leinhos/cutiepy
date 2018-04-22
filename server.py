from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Robert likes purple alligators on his undies!"
