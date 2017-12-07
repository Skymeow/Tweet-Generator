from __future__ import division, print_function
from dictogram import Dictogram
import sys, random, time

class Markov(dict):
    def __init__(self, word_list):
        self.word_list = word_list
        self.dictogram = Dictogram(word_list)
        if self.dictogram is not None:
            for item in self.dictogram:
                self.item = item

    def create_markov(self):
        corpus_dict = {}
        for i in self.dictogram:
            # get two of the index after the type we are looping through
            number = [(index+1, index+2) for index, word in enumerate(self.word_list) if word == i]
            print(number)
            # return number
        #     next_word_list = [self.word_list[num[1]] for num[1] in number if num < len(self.word_list)]
        #     corpus_dict[i] = next_word_list
        # return(corpus_dict)

    def run_markov(self, sentence_num):
        markov_dict = self.create_markov()
        print(markov_dict)
        return markov_dict
        # start = 'fish'
        # sentence_list = []
        # next_word_list = markov_dict[start]
        # sec_word = next_word_list[random.randint(0, len(next_word_list)-1)]
        # sentence_list.append(sec_word)
        # for i in range(0, sentence_num-1):
        #     next_word_list = markov_dict[sec_word]
        #     next_word = next_word_list[random.randint(0, len(next_word_list)-1)]
        #     sec_word = next_word
        #     sentence_list.append(next_word)
        # return ' '.join(sentence_list)

def test_markov_chain():
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'blue']
    mc = Markov(word_list)
    print('markov sentence: {}'.format(mc.run_markov(8)))



if __name__ == '__main__':
    test_markov_chain()

