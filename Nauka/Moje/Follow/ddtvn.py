### SPRAWDZENIE KODU POCZTOWEGO
from flask import Flask
from flask import request
from flask import render_template
from bs4 import BeautifulSoup
import urllib3
import sys


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if	request.method	==	"POST":
        start = request.form["linkstart"]
        ile_art = request.form["ile_art"]
        http = urllib3.PoolManager()
        response = http.request('GET', 'http://dziendobry.tvn.pl' + start)
        soup = BeautifulSoup(response.data, "lxml")

        tagi = {}
        kategorie = []
        tytuly = []
        leady = []
        linki = []
        linki.append(start)
        counter = 0
        liczexp = int(ile_art)

        while counter < int(ile_art):
            response = http.request('GET', 'http://dziendobry.tvn.pl' + linki[-1])
            soup = BeautifulSoup(response.data, "lxml")

            for link in soup.find_all("h4",{'class': 'detail__title'} ):
                tytuly.append(link.text.strip())

            for link in soup.find_all("div",{'class': 'detail__title-foot'} ):
                kategorie.append(link.text.strip())

            for link in soup.find_all("div",{'class': 'detail__short'} ):
                leady.append(link.text.strip())

            for link in soup.find_all("a",{'class': 'source__tag'} ):
                tagi[link.text.strip()]= link.get('href')

            for link in soup.find_all("a",{'title': 'Następny artykuł'} ):
                if not link.get('href') in linki:
                    linki.append(link.get('href'))
            counter += 1
        #DO OGRANIA!!!!
        return "DUPSKO"
        #return render_template("flaskfollow.html", tytuly=tytuly, kategorie=kategorie, leady=leady, linki=linki, liczexp=liczexp)




    else:
        return '''
        <form method="POST">
            
            <label>
				Wklej link startowy od / wideo... :
		    <input	type="text" name="linkstart">
            </label>
            
            <label>
				Ile arytkułów :
		    <input	type="text" name="ile_art">
            </label>
            
            <label>
                <input	type="submit" value="Wyślij"></input>
            </label>
        </form>
    '''

if __name__ == "__main__":
    app.run()
