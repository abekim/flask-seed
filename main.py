import os
from flask import Flask

app = Flask(__name__)

# dev mode
app.debug = True

# paths
TEMPLATE_PATH = "templates/"

@app.route("/<name>")
def hello(name="Person"):
    return render_template(TEMPLATE_PATH + "hello.html", name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = "0.0.0.0", port=port)