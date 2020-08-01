from flask import Flask
import os
from os.path import join, dirname


app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file("favicon.ico")


## おまじない
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
