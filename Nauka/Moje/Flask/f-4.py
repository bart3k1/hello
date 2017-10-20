from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/profile/<name>')
def profile(name):
    #uzywa podanego template i wrzuca podane variable 
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run()


























