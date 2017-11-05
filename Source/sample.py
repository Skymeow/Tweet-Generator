import sys, random, time

t_init = time.time()

with open('onefish.txt', 'r') as f:
    data = f.read()
    wordsList = data.split()
    # print(wordsList)
# The recipe uses module random's function uniform to get a uniformly distributed pseudo-random number between 0.0 and 1.0, then loops in parallel on items and their probabilities, computing the increasing cumulative probability, until the latter becomes greater than the pseudo-random number.
# 1. get just unique words ["one","two","fish"]
# 2. adds up frequency(token)
# randint(inclusive in both sides): [0,len-1]
# initially set word_frequency = 1
histogram_dict = {'one': 1, 'fish': 4, 'red': 1, 'two': 1, 'blue': 1}
def sample_by_frequency(histogram_dict):
# get total num of the words frequency
    total_token = sum(histogram_dict.values())
    # rand_frequency = random.randint(0, total_token)/total_token
    rand_frequency = random.uniform(0, 1)
    each_token = 0
    temp = 'word'
    for k, v in histogram_dict.items():
        each_token += v/total_token
        if each_token > rand_frequency:
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



random_words = [sample_by_frequency(histogram_dict) for _ in range(100000)]
print(check_weighted_probability(random_words))
finish = time.time()
print(finish-t_init)
