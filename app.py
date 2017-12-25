from flask import Flask
from sample import *
from markov import *
from grab_clean_file import *

app = Flask(__name__)
cleaned_file = read_file()

@app.route("/<int:population>")
def create(population=15):
    sentence = Markov(cleaned_file).generate_sentence(population)
    return sentence

if __name__ == '__main__':
    app.run()
