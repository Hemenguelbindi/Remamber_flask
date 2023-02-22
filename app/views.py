from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/dashboard.html")


@app.route("/about")
def route():
    return "<h1 style='color: red'>About!!!!!!!</h1>"