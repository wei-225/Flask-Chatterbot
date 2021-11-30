from app import app
from app.router.bot import *
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")
