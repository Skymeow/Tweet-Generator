from __future__ import division, print_function
from dictogram import Dictogram
from sample import sample_by_frequency
import sys, random, time
from grab_clean_file import read_file
import re

class Markov(dict):
    def __init__(self, word_list):
        self.markov_chain = self.create_histograms(word_list)

    def generate_start(self, word_list):
        result = []
        for i in range(0, len(word_list) - 2):
            if word_list[i] == 'END':
                result.append(word_list[i+1])
        return result

    def create_histograms(self, word_list):
        """Read the given word list and create the Markov chain structure.
        Loop over the words, two at a time (word, next_word).
        If word has never been seen before, create a new histogram.
        Otherwise, if word has been seen, get its existing histogram.
        In either case, add count 1 for next_word in word's histogram."""
        histograms = {}
        histograms['END'] = Dictogram(self.generate_start(word_list))
        for index, word in enumerate(word_list):
            # If word has never been seen before, create a new histogram with a list containing next word
            if index < len(word_list) - 1:
                next_word = word_list[index+1]
                if word not in histograms:
                    histograms[word] = Dictogram([next_word])
                # if word has been seen, get its existing histogram and append the count to it
                else:
                    histograms[word].add_count(next_word) # o(n) , n is len word_list
        return histograms

    def generate_word(self, markov):
    #     """Given the last word generated in a sentence, pick a new word
    #     randomly according to the frequency of words following it."""
        current_word = 'END'
        while current_word == 'END':
            current_word = sample_by_frequency(markov['END'])
            return current_word
        return random.choice(markov.keys())

    def generate_sentence(self, num_words=10):
        """Perform a random walk on this Markov chain to generate a
        sequence of words and return it as a single formatted string."""
        # TODO: Loop and generate num_words, collect each in a list
        # TODO: Format the list of words as a sentence and return it
        #
        current_word = self.generate_word(self.markov_chain)
        sentence_list = [current_word.capitalize()]
        # generate the sentence with the length of num_words
        for i in range(0, num_words):
            # get the next word based on frequency and add that to the sentence
            current_histogram = self.markov_chain[current_word]
            random_weighted_word = sample_by_frequency(current_histogram)
            current_word = random_weighted_word
            sentence_list.append(current_word)
        # change the end of the sentence into . or , depends on if the sentence is ended2
        for index, word in enumerate(sentence_list):
            if index == (len(sentence_list)-1) and word == 'END':
                sentence_list[index] = "."
                # sentence = re.sub(' END', '.', sentence, flags=re.IGNORECASE)
            elif word == "END":
                # sentence = re.sub(' END', ',', sentence, flags=re.IGNORECASE)
                sentence_list[index] = ","
        sentence = ' '.join(sentence_list) + '.'
        print(sentence)
        return sentence

def test_markov_chain():
    cleaned_file = read_file("pages.txt")
    markov_model = Markov(cleaned_file)
    # print(Markov(cleaned_file).generate_word(Markov(cleaned_file).markov_chain))
    print(markov_model.generate_sentence())
    # print('markov sentence: {}'.format(Markov(word_list).generate_sentence()))

if __name__ == '__main__':
    test_markov_chain()

