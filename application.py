from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "<p>Hello, World!</p> How things are going??"

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run()