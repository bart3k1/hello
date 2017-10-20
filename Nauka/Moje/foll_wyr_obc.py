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
        http = urllib3.PoolManager()
        response = http.request('GET', "http://www.edupedia.pl/map/dictionary/id/8_slownik_wyrazow_obcych.html")
        soup = BeautifulSoup(response.data, "lxml")

        linki = []
        tytuly = []
        ile_art = request.form["ile_art"]
        liczexp = []

        for i in range(int(ile_art)):
            liczexp.append(randint(0,10571))

        for link in soup.find_all("a",{'class': 'lkyDescLink'} ):
            tytuly.append(link.text.strip())
        tytuly_export = tytuly[11:]

        for link in soup.find_all("a",{'class': 'lkyDescLink'} ):
                linki.append(link.get('href'))
        linki_exp = linki[11:]

        return render_template("arty_obce.html", tytuly=tytuly_export, linki=linki_exp, liczexp=liczexp)




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
