from app import app
from flask import render_template, request, redirect


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template('public/about.html')


@app.route("/sign_up", methods=["GET", "POST"])
def sing_up():

    if request.method  == "POST":
        req = request.form
        username = req["username"]
        mail = req['email']
        password = req['password']
        print(username, mail, password)
        return redirect(request.url)

    return render_template("public/sign_up.html")