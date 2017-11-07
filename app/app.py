from flask import Flask
from sample import *

app = Flask(__name__)

@app.route("/<int:population>")
def create(population=1):
    return create_random_sentence(population)

if __name__ == '__main__':
    app.run(debug=True)
