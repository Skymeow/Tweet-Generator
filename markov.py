from __future__ import division, print_function
from dictogram import Dictogram

class Markov(dict):
    def __init(self, word_list=None):
        super(Markov, self).__init__()
        dictogram = Dictogram(self.fish_words)
        print(dictogram)
        if dictogram is not None:
            for item in dictogram:
                self.create_markov(item)

    def create_markov(self, item, word_list):
        corpus_dict = {}
        number = [(index+1) for index, word in enumerate(word_list) if word == item]
        next_word_list = [word_list[num] for num in number if num < len(word_list)]
        corpus_dict[item] = next_word_list
    return(corpus_dict)
