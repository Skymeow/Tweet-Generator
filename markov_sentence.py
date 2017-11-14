import sys, random, time
import histogram
from dictogram import Dictogram

wordsList = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
def token_corpus(wordsList):
    histogram_dict = histogram.histogram_dict(wordsList)
    # start = wordsList[0]
    # end = wordsList[len(wordsList)-1]
    corpus_dict = {}
    for i in histogram_dict:
        number = [(index+1) for index, word in enumerate(wordsList) if word == i]
        next_word_list = [wordsList[num] for num in number if num < 8]
        corpus_dict[i] = next_word_list
    return(corpus_dict)
# {'blue': ['fish'], 'fish': ['two', 'red', 'blue'], 'two': ['fish'], 'red': ['fish'], 'one': ['fish']}


def run_markov(sentence_num):
    markov_dict = token_corpus(wordsList)
    start = 'fish'
    sentence_list = []
    sec_word = ''
    for i in range(0, sentence_num):
        # rand_word = wordsList[random.randint(0, sentence_num)]
        if i <= 1:
            next_word_list = markov_dict[start]
            sec_word = next_word_list[random.randint(0, len(next_word_list)-1)]
            sentence_list.append(sec_word)
            # print('first if', sentence_list)
        else:
            next_word_list = markov_dict[sec_word]
            next_word = next_word_list[random.randint(0, len(next_word_list)-1)]
            sec_word = next_word
            sentence_list.append(next_word)
    return ' '.join(sentence_list)

print(run_markov(10))
