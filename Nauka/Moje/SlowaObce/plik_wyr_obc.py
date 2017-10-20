from flask import Flask
from flask import request
from flask import render_template
from bs4 import BeautifulSoup
import urllib3
from random import randint


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if	request.method	==	"POST":

        slowa = []
        linki = []
        ile_art = request.form["ile_art"]
        liczexp = []
        for i in range(int(ile_art)):
            liczexp.append(randint(0,10571))

        with open('slowa_obce.txt', 'r') as f:
            for line in f:
                slowa.append(line.strip())

        with open('slowa_obce_linki.txt', 'r') as f:
            for line in f:
                linki.append(line.strip())

        return render_template("arty_obce_tekst.html", slowa=slowa, linki=linki, liczexp=liczexp)




    else:
        return '''
        <form method="POST">
            
            <label>
			Ile słówek :
		    <input	type="text" name="ile_art">
            </label>
            
            <label>
                <input	type="submit" value="Wyślij"></input>
            </label>
        </form>
    '''

if __name__ == "__main__":
    app.run()
