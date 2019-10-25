from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route("/")
def hello():
  tot = {
    "ok": True,
    "error": False    
        }
  return jsonify(tot)