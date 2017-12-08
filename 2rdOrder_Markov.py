from __future__ import division, print_function
from dictogram import Dictogram
from sample import sample_by_frequency
import sys, random, time

class Markov(dict):
    def __init__(self, word_list):
        self.markov_chain = self.create_histograms(word_list)

    def create_histograms(self, word_list):
        """Read the given word list and create the Markov chain structure.
        Loop over the words, three at a time (previous_word, word, next_word).
        """
        histograms = {}
        # since it's 2rd order, we are making space for 2 words
        for index, word in enumerate(word_list):
            # If word has never been seen before, create a new histogram with a list containing next word
            if index < len(word_list) - 2:
                window = (word_list[index], word_list[index+1])
                if window not in histograms:
                    histograms[window] = Dictogram([word_list[index+2]])
                # if word has been seen, get its existing histogram and append the count to it
                else :
                    histograms[window].add_count(word_list[index+2]) # o(n) , n is len word_list
        print(histograms)
        return histograms

    def generate_sentence(self, num_words=10):
        """Perform a random walk on this Markov chain to generate a
        sequence of words and return it as a single formatted string."""
        sentence_list = []
        current_window = ('one', 'fish')
        for i in range(0, num_words):
            next_random_word = self.generate_word(current_window)
            current_window = (current_window[1], next_random_word)
            sentence_list.append(next_random_word)
        return ' '.join(sentence_list)

    def generate_word(self, last_window):
        """Given the last word generated in a sentence, pick a new word
        randomly according to the frequency of words following it."""
        current_histogram = self.markov_chain[last_window]
        # Sample a word from that histogram by word frequency
        next_weighted_word = sample_by_frequency(current_histogram)
        return next_weighted_word

def test_markov_chain():
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'blue']
    Markov(word_list)

    print('markov sentence: {}'.format(Markov(word_list).generate_sentence()))



if __name__ == '__main__':
    test_markov_chain()

