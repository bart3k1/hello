from flask import Flask

#flask object, name - root path
app = Flask(__name__)

#connect (url) web page - root directory - to return value
#decorator - wrap a function modify its behavior
@app.route('/') #/about itd
#index - homepage, albo about itd
def index():
    return ">>>Homepage<<<"

@app.route('/druga')
#druga do drugiej
def druga():
    return ">>><h2>Druga Strona</h2><<<"

@app.route('/druga/trzecia')
#trzecia do trzeciej pod druga
def trzecia():
    return ">>><h3>Trzecia Strona</h3><<<"

@app.route('/profile/<username>')
#variable!!
def profile(username):  #variable
    return "Hello {}".format(username)

#integery trzba zajawić
@app.route('/post/<int:post_id>')
#variable!!
def post(post_id):  #variable
    return "POST -  {}".format(post_id)

#kick off server
if __name__ == "__main__":
    app.run(debug=True) #developer mode

























