import re
from pathlib import Path
import sys, random, time
from nltk.tokenize import sent_tokenize


def read_file():
    result_list = []
    raw_file = Path("cleaned_shining.txt")
    sentence_list = open(raw_file).read().lower()
    sentence_list = remove_nonsense(sentence_list)
    cleaned_sentences = sent_tokenize(sentence_list)
    for sentence in cleaned_sentences:
        if sentence[0] != ".":
            add_end = sentence[:-1]
            # remove_dot = sentence[:-1]
            # add_end = remove_dot + ' END'
            result_list.append(add_end)
    return result_list

def remove_nonsense(text):
    cleaner = re.sub(r'\(', ' ', text)
    cleaner = re.sub(r'\)', ' ', cleaner)
    cleaned = re.sub('--', ' ', cleaner)
    return cleaner

# print(read_file())
