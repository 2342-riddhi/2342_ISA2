#app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def roll_no():
    return "Roll no: 2342"