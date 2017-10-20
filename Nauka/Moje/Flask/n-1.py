from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/slashboard')
@app.route('/dashboard')
def dashboart():
    return render_template("dashboard.html")


@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef', 'Bzdety inne']
    return render_template("shopping.html", food=food)


if __name__ == "__main__":
    app.run()

























