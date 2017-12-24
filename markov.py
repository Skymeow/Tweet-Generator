from __future__ import division, print_function
from dictogram import Dictogram
from sample import sample_by_frequency
import sys, random, time
from grab_clean_file import read_file

class Markov(word_list):
    def __init__(self, word_list):
        # for sentence in word_list: # Cleaned Corpus
        self.markov_chain = self.create_histograms(word_list)

    def create_histograms(self, word_list):
        """Read the given word list and create the Markov chain structure.
        Loop over the words, two at a time (word, next_word).
        If word has never been seen before, create a new histogram.
        Otherwise, if word has been seen, get its existing histogram.
        In either case, add count 1 for next_word in word's histogram."""
        histograms = {}
        start_list =  create_start_list(word_list)
        histograms['START'] = Dictogram(start_list)
        for index, word in enumerate(word_list):
            # If word has never been seen before, create a new histogram with a list containing next word
            if index < len(word_list) - 1:
                if word not in self:
                    histograms[word] = Dictogram([word_list[index+1]])
                # if word has been seen, get its existing histogram and append the count to it
                else :
                    histograms[word].add_count(word_list[index+1]) # o(n) , n is len word_list
        return histograms

    def generate_sentence(self, num_words=10):
        """Perform a random walk on this Markov chain to generate a
        sequence of words and return it as a single formatted string."""
        # TODO: Loop and generate num_words, collect each in a list
        # TODO: Format the list of words as a sentence and return it
        current_word = self.generate_word(self.markov_chain)
        sentence_list = [current_word]
        for i in range(0, num_words):
            current_histogram = self.markov_chain[current_word]
            random_weighted_word = sample_by_frequency(current_histogram)
            current_word = random_weighted_word
            sentence_list.append(current_word)
        sentence_list[0] = sentence_list[0].capitalize()
        return ' '.join(sentence_list) + '.'
        # return sentence_list

    def generate_word(markov):
    #     """Given the last word generated in a sentence, pick a new word
    #     randomly according to the frequency of words following it."""
        for word in markov:
            if word != 'START':
                current_histogram = self.markov_chain[word]
                next_weighted_word = sample_by_frequency(current_histogram)
        return next_weighted_word
        # current_word = grab_clean_file.create_start_list()
        # current_histogram = self.markov_chain[current_word]
        # next_weighted_word = sample_by_frequency(current_histogram)
        # return next_weighted_word

    def create_start_list(data):
        for sentence in data:
            sentence_separate = sentence.split(' ')
            start_list  = [].append(sentence_separate[0])
        return start_list

def test_markov_chain():
    # word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'blue']
    cleaned_file = grab_clean_file.read_file()
    # start_word = grab_clean_file.create_start_list()
    markov_modal = Markov(cleaned_file)
    print(markov_modal.generate_sentence())
    # print('markov sentence: {}'.format(Markov(word_list).generate_sentence()))



if __name__ == '__main__':
    test_markov_chain()

