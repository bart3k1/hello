from flask import Flask
from flask import render_template

app = Flask(__name__)

#2 rozne urle connectujemy do indexa i rendera
@app.route('/')# and not logged
@app.route('/<user>') #logged
def index(user=None): #None jesli not logged
    return render_template("user.html", user=user)

@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef', 'Bzdety inne']
    return render_template("shopping.html", food=food)


if __name__ == "__main__":
    app.run()

























