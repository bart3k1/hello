from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Metod used: {}".format(request.method)


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You're using POST"
    else:
        return "Using GET"

if __name__ == "__main__":
    app.run(debug=True)

























