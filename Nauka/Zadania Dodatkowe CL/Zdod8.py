from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)
fon = {"a" : 123, "b" : 456}

@app.route('/', methods=['GET', 'POST'])
def index():
    if	request.method	==	"POST":
        name = request.form["name"]
        number = request.form["number"]
        fon[name] = number
        return "{} : {} dodane do książki".format(name, number)

    else:
         return render_template("telefon.html", fon=fon)

if __name__ == "__main__":
    app.run()
