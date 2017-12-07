from __future__ import division, print_function
from dictogram import Dictogram
from sample import sample_by_frequency
import sys, random, time

class Markov(dict):
    def __init__(self, word_list):
        self["START"] = Dictogram()
        self.create_histograms(word_list)

    def create_histograms(self, word_list):
        """Read the given word list and create the Markov chain structure.
        Loop over the words, two at a time (word, next_word).
        If word has never been seen before, create a new histogram.
        Otherwise, if word has been seen, get its existing histogram.
        In either case, add count 1 for next_word in word's histogram."""
        # TODO
        for index, word in enumerate(word_list):
            # If word has never been seen before, create a new histogram with a list containing next word
            self["START"].add_count(word_list[0])
            if index < len(word_list) - 1:
                if word not in self:
                    self[word] = Dictogram([word_list[index+1]])
                # if word has been seen, get its existing histogram and append the count to it
                else :
                    self[word].add_count(word_list[index+1]) # o(n) , n is len word_list
            self[word_list[-1]] = Dictogram("END")

        # print(histograms)


    def generate_sentence(self, num_words=10):
        """Perform a random walk on this Markov chain to generate a
        sequence of words and return it as a single formatted string."""
        # TODO: Loop and generate num_words, collect each in a list
        # TODO: Format the list of words as a sentence and return it
        sentence_list = []
        current_word = "one"
        for i in range(0, num_words):
            next_random_word = self.generate_word(current_word)
            current_word = next_random_word
            sentence_list.append(current_word)
        return ' '.join(sentence_list)

    def generate_word(self, last_word):
        """Given the last word generated in a sentence, pick a new word
        randomly according to the frequency of words following it."""
        # TODO: Find the histogram representing last word's transitions
        # TODO: Sample a word from that histogram by word frequency
        # TODO: Return that word (string)
        current_histogram = self[last_word]
        next_weighted_word = sample_by_frequency(current_histogram)
        return next_weighted_word

    # def generate_sentence_at_once(self, num_words=10):
    #     current_word = "one"
    #     sentence_list = [current_word]
    #     for i in range(0, num_words):
    #         current_histogram = self.markov_chain[current_word]
    #         next_weighted_word = sample_by_frequency(current_histogram)
    #         current_word = next_weighted_word
    #         sentence_list.append(current_word)
    #     return ' '.join(sentence_list)

def test_markov_chain():
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'blue']
    Markov(word_list)

    print('markov sentence: {}'.format(Markov(word_list).generate_sentence()))



if __name__ == '__main__':
    test_markov_chain()

