from flask import Flask

#flask object, name - root path
app = Flask(__name__)

#connect web page - root directory
@app.route('/') #/about itd
#index - homepage, albo about itd
def index():
    return ">>>Homepage<<<"

#kick off server
if __name__ == "__main__":
    app.run(debug=True) #developer mode

























