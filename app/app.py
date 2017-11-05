from flask import Flask
from sample import *

app = Flask(__name__)

@app.route("/")
def create():
    return create_random_sentence(12)

if __name__ == '__main__':
    app.run(debug=True)
