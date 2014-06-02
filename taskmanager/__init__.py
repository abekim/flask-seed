from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.debug = True

app.config["MONGODB_SETTINGS"] = {
    'DB': 'Tasks'
}

db = MongoEngine(app)

@app.route("/")
def hello():
    return render_template("index.html", title="Welcome")
