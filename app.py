import os
from wsgiref import simple_server
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
@cross_origin()
def index():
    return "initial app setup"

port = int(os.getenv("PORT", 5000))

if __name__ == "__main__":
    host = "0.0.0.0"
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()