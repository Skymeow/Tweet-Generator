import re
from pathlib import Path
import sys, random, time
from nltk.tokenize import sent_tokenize


def read_file():
    start_list = []
    raw_file = Path("cleaned_shining.txt")
    cleaned_sentences = open(raw_file).read().lower()
    cleaned_sentences = remove_nonsense(cleaned_sentences)
    sentence_list = sent_tokenize(cleaned_sentences)
    words = cleaned_sentences.split(" ")
    for sentence in sentence_list:
        if sentence[0] != ".":
            start = sentence.split(" ")[0].capitalize()
            start_list.append(start)
    return {'start_list': start_list, 'word_list': words}

def remove_nonsense(text):
    cleaner = re.sub(r'\(', ' ', text)
    cleaner = re.sub(r'\)', ' ', cleaner)
    cleaned = re.sub('--', ' ', cleaner)
    return cleaner

# print(read_file()['word_list'])
