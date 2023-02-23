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
    age = 31
    langs = ['Python', 'Javascript', 'Bash', 'C', 'Rust']
    friends = {
        "Tom": 30,
        "Amy": 60,
        "Tony": 56,
        "Clarissa": 23,
    }
    colors = ('Red', "Green")

    coll = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pullin repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name='Flask Jinja',
        description='Template desing tutorial',
        url='https://github.com/Hemenguelbindi/Remamber_flask'
    )

    def repid(x, q):
        return x * q

    return render_template(
        'public/jinja.html',
        my_name=my_name,
        age=age,
        langs=langs,
        friends=friends,
        colors=colors,
        coll=coll,
        my_remote=my_remote,
        repid=repid
    )