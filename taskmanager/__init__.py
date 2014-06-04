from flask import Flask, render_template, jsonify, request
from flask.ext.mongoengine import MongoEngine
from taskmanager.json_encoder import MongoEngineJSONEncoder

app = Flask(__name__)
app.debug = True
app.json_encoder = MongoEngineJSONEncoder

app.config["MONGODB_SETTINGS"] = {
    'DB': 'Tasks'
}

if not app.debug:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)

db = MongoEngine(app)

from taskmanager.models import Task

@app.route("/")
def hello():
    return render_template("index.html", title="Welcome", tasks=Task.objects())

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        app.logger.info("New task, \"%s\" added", request.form['description'])
        description = request.form['description']

        t = Task(description=description)

        t.save()
    return jsonify(data=t)
