from __future__ import division, print_function
from pprint import pprint
import sys, random, time
import re

from dictogram import Dictogram
from sample import sample_by_frequency
from grab_clean_file import read_file


class Markov(object):
    def __init__(self, word_list):
        self.histograms = self.create_histograms(word_list)

    def generate_start(self, word_list):
        result = []
        for i in range(0, len(word_list) - 2):
            if word_list[i] == 'END':
                result.append(word_list[i+1])
                # result.append(word_list[i+2])
        return result

    def create_histograms(self, word_list):
        """Read the given word list and create the Markov chain structure.
        Loop over the words, three at a time (previous_word, word, next_word).
        """
        histograms = {}
        histograms['END'] = Dictogram(self.generate_start(word_list))
        # since it's 2rd order, we are making space for 2 words
        for index, word in enumerate(word_list):

            # if word == 'END':
            #     window = ('END', word_list[index+1])
            if index < len(word_list) - 2:
                prev_word = word_list[index]
                current_word = word_list[index+1]
                next_word = word_list[index+2]
                window = (prev_word, current_word)
                # If word has never been seen before, create a new histogram with a list containing next word
                if window not in histograms:
                    histograms[window] = Dictogram([next_word])
                # if word has been seen, get its existing histogram and append the count to it
                else :
                    histograms[window].add_count(next_word) # o(n) , n is len word_list
        # pprint(histograms)
        return histograms

    def generate_sentence(self, num_words=10):
        """Perform a random walk on this Markov chain to generate a
        sequence of words and return it as a single formatted string."""
        start_word = self.generate_word(self.histograms)
        current_window = ('END', start_word)
        sentence_list = [start_word.capitalize()]
        # generate the sentence with the length of num_words
        # change it into a while loop to make sure it stops when the random_weighted_word is 'end'
        random_weighted_word = ''
        for i in range(0, num_words):
        # while random_weighted_word != 'END':
            # get the next word based on frequency and add that to the sentence
            current_histogram = self.histograms[current_window]
            random_weighted_word = sample_by_frequency(current_histogram)
            if random_weighted_word != 'END':
                sentence_list.append(random_weighted_word)
                # print(sentence_list)
            else:
                break
            # reassign the current window
            prev_word = current_window[1]
            current_window = (prev_word, random_weighted_word)
        # change the end of the sentence into . or , depends on if the sentence is ended2
        for index, word in enumerate(sentence_list):
            if index == (len(sentence_list)-1) and word == 'END':
                sentence_list[index] = "."
                # sentence = re.sub(' END', '.', sentence, flags=re.IGNORECASE)
            elif word == "END":
                # sentence = re.sub(' END', ',', sentence, flags=re.IGNORECASE)
                sentence_list[index] = ","
        sentence = ' '.join(sentence_list) + '.'
        # print(sentence)
        return sentence

    def generate_word(self, markov):
    #     """Given the last word generated in a sentence, pick a new word
    #     randomly according to the frequency of words following it."""
        current_word = 'END'
        while current_word == 'END':
            current_word = sample_by_frequency(markov['END'])
            return current_word
        return random.choice(markov.keys())


def test_markov_chain():
    file_name = "pages.txt"
    # file_name = "taco.txt"
    cleaned_file = read_file(file_name)
    markov_model = Markov(cleaned_file)
    # pprint(markov_model.histograms)
    # print(Markov(cleaned_file).generate_word(Markov(cleaned_file).histograms))
    print(markov_model.generate_sentence())
    # print('markov sentence: {}'.format(Markov(word_list).generate_sentence()))

if __name__ == '__main__':
    test_markov_chain()
