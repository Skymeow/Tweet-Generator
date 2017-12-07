import sys, random, time
import histogram
from dictogram import Dictogram
t_init = time.time()

with open('onefish.txt', 'r') as f:
    data = f.read()
    wordsList = data.split()

histogram_dict = histogram.histogram_dict(wordsList)

def sample_by_frequency(histogram_dict):
    # get total num of the words frequency
    if isinstance(histogram_dict, Dictogram):
        total_token = histogram_dict.tokens
    else:
        total_token = sum(histogram_dict.values())
    # rand_frequency = random.randint(0, total_token)/total_token
    rand_frequency = random.uniform(0, 1)
    weighted_token = 0
    for k, v in histogram_dict.items():
        weighted_token += v/total_token
        if weighted_token > rand_frequency:
            return k

# check how many time the word appears in the 10000 calls
def check_weighted_probability(random_words):
    words_histogram = {}
    for word in random_words:
        if word in words_histogram:
            words_histogram[word] += 1
        else:
            words_histogram[word] = 1
    return words_histogram

def create_random_sentence(sentence_length):
    random_words = [sample_by_frequency(histogram_dict) for _ in range(sentence_length)]
    return ' '.join(random_words)

# print(create_random_sentence(5))
# print(check_weighted_probability(random_words))
# random_words = [sample_by_frequency(histogram_dict) for _ in range(0, 10)]
# finish = time.time()
# print(finish-t_init)
