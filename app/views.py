from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template('public/about.html')


@app.route("/jinja")
def jinja():
    my_name = "Victor"
    return render_template('public/jinja.html', my_name=my_name)