import re
from pathlib import Path
import sys, random, time
from nltk.tokenize import sent_tokenize


def read_file():
    cleaned_corp = []
    raw_file = Path("new_shining.txt")
    file_open = open(raw_file).read()
    cleaner = re.sub(r'\(', '', file_open)
    cleanerer = re.sub(r'\)', '', cleaner)
    cleanererer = re.sub(r'\d*', '', cleanerer)
    corpus = sent_tokenize(cleanererer)
    for sentence in corpus:
        if sentence[0] != ".":
            cleaned_corp.append(sentence)
    return cleaned_corp

    # print(cleaned_corp)
     # no_quote= re.sub('"', "",file_open)
    # no_space = re.sub('\n', "", no_quote)
    # no_weird = re.sub('\(\)'), "", no_quote)
    # re.match(r'', re.I, re.)
    # f = open("shining.txt", "w")
    # f.write(no_space)
print(read_file())
