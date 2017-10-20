from flask import Flask
from flask import request
from flask import render_template

pizza = {
'FIT MARGHERITA' : [ 'świeże pomidory', 'pesto'] ,
'PROSCIUTTO' : [ 'szynka'] ,
'CAPRICCIOSA' : [ 'szynka', 'pieczarki'] ,
'PARMIGIANA ' : [ 'bakłażan' , 'parmezan'] ,
'POLLO ' : [ 'kurczak', 'ananas', 'kukurydza'] ,
'MISTA ' : [ 'wołowina', 'kurczak pieczony', 'papryka pepperoni', 'pieczarki', 'cebula'],
'PERE E NOCI' : [ 'gruszka', 'gorgonzola', 'orzechy włoskie'] ,
'HAWAII ' : [ 'szynka', 'ananas'] ,
'ROMA ' : [ 'kiełbasa pepperoni', 'boczek', 'pieczarki', 'cebula'] ,
'AL TONNO ' : [ 'tuńczyk', 'oliwki', 'cebula', 'kapary'] ,
'VEGETARIANA ' : [ 'papryka', 'pieczarki', 'oliwki', 'cebula', 'kukurydza'] ,
'CACCIATORE ' : [ 'salami', 'oliwki', 'czerwona cebula', 'gorgonzola'] ,
'RUCOLA E COCTAIL DI GAMBERETTI ' : [ 'krewetki', 'oliwki', 'rucola', 'czosnek', 'parmezan'] ,
'FRUTTI DI MARE ' : [ 'małże' , 'krewetki', 'kalmary'] ,
'SWEET BACON ' : [ 'boczek', 'szpinak', 'żurawina', 'gruszka', 'ser pleśniowy'] ,
'AL CAPONE ' : [ 'salami', 'pieczarki', 'cebula', 'czosnek', 'papryka pepperoni'] ,
'PRIMERA' : [ 'boczek', 'kabanos', 'pieczarki', 'cebula'] ,
'DUO HAWAII' : [ 'szynka', 'polędwica', 'ananas', 'brzoskwinia'] ,
'QUATTRO FORMAGGI ' : [ 'mozzarella', 'cheddar', 'lazur', 'parmezan'] ,
'PRIMAVERA ' : ['szynka dojrzewająca', 'rucola', 'świeży pomidor', 'anchovies', 'kapary'],
'CARBONARA' : [ 'boczek', 'cebula', 'czosnek', 'jajko', 'parmezan'] ,
'PEPPERONI ' : [ 'szynka', 'kiełbasa pepperoni', 'oliwki', 'cebula', 'papryka pepperoni'] ,
'PHILADELPHIA ' : [ 'szynka', 'salami', 'polędwica', 'pomidor', 'papryka', 'kukurydza'] ,
'QUATTRO CARNI ' : [ 'szynka', 'salami', 'kabanos', 'wołowina'] ,
'RAPINA ' : [ 'oscypek', 'żurawina', 'cebula', 'boczek'] ,
'KILLER PIZZA ' : [ 'kiełbasa pepperoni', 'salami', 'cebula', 'papryka jalapeno', 'kukurydza', 'chili'] ,
'FIT PROSCIUTTO ' : [ 'szynka dojrzewająca', 'suszony pomidor', 'rucola', 'parmezan'],
'NORDIC ' : [ 'łosoś wędzony', 'ser mascarpone', 'kapary', 'świeży koper'] ,
'MESSICANA ' : [ 'wołowina', 'papryka jalapeno', 'cebula', 'czerwona fasola', 'tabasco'],
'ORIGINAL PEPPERONI ' : [ 'kiełbasa pepperoni'] ,
'GRECIA ' : [ 'pomidor', 'ser feta', 'oliwki', 'cebula', 'papryka', 'sos czosnkowy']
}

skladniki = ['boczek', 'szpinak', 'żurawina', 'gruszka', 'ser pleśniowy', 'szynka', 'pieczarki', 'kiełbasa pepperoni', 'salami', 'cebula', 'papryka jalapeno', 'kukurydza', 'chili', 'czosnek', 'papryka pepperoni', 'polędwica', 'pomidor', 'papryka', 'kabanos', 'wołowina', 'ser feta', 'oliwki', 'sos czosnkowy', 'ananas', 'brzoskwinia', 'mozzarella', 'cheddar', 'lazur', 'parmezan', 'kurczak pieczony', 'łosoś wędzony', 'ser mascarpone', 'kapary', 'świeży koper', 'krewetki', 'rucola', 'szynka dojrzewająca', 'świeży pomidor', 'anchovies', 'tuńczyk', 'suszony pomidor', 'kurczak', 'czerwona cebula', 'gorgonzola', 'oscypek', 'świeże pomidory', 'pesto', 'orzechy włoskie', 'czerwona fasola', 'tabasco', 'jajko', 'bakłażan', 'małże', 'kalmary']
skla_sort = sorted(skladniki)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if	request.method	==	"POST":
        wybrany_skladnik = request.form["wybrany_skladnik"]
        #return "{}".format(wybrany_skladnik)
        p = []
        s= []
        for k,v in pizza.items():
            if wybrany_skladnik in v:
                p.append(k)
                s.append(v)
        dlugosc = len(p)
        return render_template("pizza.html", p=sorted(p), s=s, dlugosc=dlugosc)
            #"ZAMÓW: {} {}".format(p, s)

    else:
        return render_template("pizzaPOST.html", skladniki=skladniki, skla_sort=skla_sort)

if __name__ == "__main__":
    app.run()
