from flask import Flask
from sample import *
from markov import *
from grab_clean_file import *
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    cleaned_file = read_file()
    random_sentence = Markov(cleaned_file).generate_sentence()
    return render_template('index.html', sentence=random_sentence)

@app.route("/<int:population>")
def create(population=10):
    cleaned_file = read_file()
    sentence = Markov(cleaned_file).generate_sentence(population)
    return sentence

if __name__ == '__main__':
    app.run()
