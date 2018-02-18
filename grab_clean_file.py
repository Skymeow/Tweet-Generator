import re
from pathlib import Path
import sys, random, time
# from nltk.tokenize import sent_tokenize

def read_file(file_name):
    start_list = []
    raw_file = Path(file_name)
    cleaned_sentences = open(raw_file).read().lower()
    cleaned_sentences = remove_nonsense(cleaned_sentences)
    matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*",cleaned_sentences)
    return ['END'] + matches

def remove_nonsense(text):
    cleaner = re.sub(r'\. . . ', ' ', text)
    cleaner = re.sub(r'\... ', ' ', cleaner)
    cleaner = re.sub(r'\- ', ' ', cleaner)
    cleaner = re.sub(r'\?', ' . ', cleaner)
    cleaner = re.sub(r'\!', ' , ', cleaner)
    cleaner = re.sub('\.\s+', ' END ', cleaner)
    return cleaner

# print(read_file())
