import random, sys

with open('/usr/share/dict/words', 'r') as f:
    data = f.read()
    # splits at space
    dataList = data.split()

raw_sentence = "one fish two fish red fish blue fish"
sentence = raw_sentence.split()
list_result = []
group_count = []
def histogram_list(sentence):
# stores each unique word and number of times the word appears
#1 as a list of list
    for i in range(0, len(sentence)-1):
        item = sentence[i]
        occurence = sentence.count(item)
        first_list = [item, occurence]
        # prevent adding duplicated item to the list
        if first_list not in list_result:
            list_result.append(first_list)
    print(list_result)

histogram_list(sentence)

# replacing a elemeny in tuples is more expensive than in a list
tuple_result = []
def histogram_tuples(sentence):
    for item in sentence:
        occurence = sentence.count(item)
        first_tuple = (item, occurence)
        if first_tuple not in tuple_result:
            tuple_result.append(first_tuple)
    print(tuple_result)

histogram_tuples(sentence)

dict_result = {}
def histogram_dict(sentence):
    for item in sentence:
        occurence = sentence.count(item)
        # since key in dict has to be unique, we don't need to worry about duplicate
        dict_result[item] = occurence
    return(dict_result)

histogram_dict(sentence)

# group_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]
def group_histogram(sentence):
    flattened_list = []
    # group_count = []
    for item in sentence:
        occurence = sentence.count(item)
        if item not in flattened_list:
            flattened_list.append(item)
            flattened_list.append(occurence)
        # get the word and occurence in the same level of a dict
    print(flattened_list)

    # group the words by occurence in a tuple and put tuples into a dict
    for current_index in range(1, len(flattened_list), 2):
        # if occurence already exist in group_count, get the words that has the same occurence
        if flattened_list[current_index] in group_count:
            # get the duplicated frequency of words
            temp_count = flattened_list[current_index]
            # get the position of the frequency's matching dict words
            append_word_index = group_count.index(temp_count) + 1
            # get the word in flattened list with the same frequency
            append_word = flattened_list[current_index-1]
            # append the word to dict in the result list
            group_count[append_word_index].append(append_word)
        else:
            # append the tuple with the unique occurence as first element, dict of words as second
            # group_count.append((flattened_list[current_index], flattened_list[current_index-1]))
            group_count.append(flattened_list[current_index])
            group_count.append([flattened_list[current_index-1]])
    return(group_count)

group_histogram(sentence)

print("YOOOOOO", group_count)
def unique_words(group_count):
    print("HII", len(group_count))
    for i in range(0,len(group_count)):
        print(group_count[i])
        if group_count[i] == 1:
            result_word = group_count[i+1]
        unique_words_count = len(result_word)
    print(unique_words_count)
    return unique_words_count

unique_words(group_count)

def frequency(word, group_count):
    for i in range(1, len(group_count), 2):
        if word in group_count[i]:
            frequency_count = group_count[i-1]
    print(frequency_count)

frequency('fish', group_count)



