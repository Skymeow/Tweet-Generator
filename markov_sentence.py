import sys, random, time
import histogram
from dictogram import Dictogram
import pprint
wordsList = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'blue']
def token_corpus(wordsList):
    histogram_dict = histogram.histogram_dict(wordsList)
    corpus_dict = {}
    for i in histogram_dict:
        number = [(index+1) for index, word in enumerate(wordsList) if word == i]
        next_word_list = [wordsList[num] for num in number if num < len(wordsList)]
        corpus_dict[i] = next_word_list
    print(corpus_dict)
    return(corpus_dict)

def run_markov(sentence_num):
    markov_dict = token_corpus(wordsList)
    start = 'fish'
    sentence_list = []
    next_word_list = markov_dict[start]
    sec_word = next_word_list[random.randint(0, len(next_word_list)-1)]
    sentence_list.append(sec_word)
    for i in range(0, sentence_num-1):
        next_word_list = markov_dict[sec_word]
        next_word = next_word_list[random.randint(0, len(next_word_list)-1)]
        sec_word = next_word
        sentence_list.append(next_word)
    return ' '.join(sentence_list)

print(run_markov(10))
