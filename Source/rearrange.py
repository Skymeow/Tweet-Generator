import random, sys



def random_python(words):
    result = []
    for i in range(0, len(words)):
        rand_index = random.randint(0, len(words)-1)
        print(words.pop(rand_index))
        result.append(words.pop(rand_index))
    return(' '.join(result))

def reverse_word(letters):
    result = letters[::-1]
    return result

def mad_libs(words):
    result = []
    for i in range(0, len(words)):
        rand_index = random.randint(0, len(words)-1)
        result.append(words.pop(rand_index))
    print(result)
    k = len(result)
    part1 = "Today we are celebrating #%s"%result[k-1]
    part2 = " with #%s"%result[k-2]
    part3 = " having a #%s."%result[k-3]
    sentence = part1 + part2 + part3
    print(sentence)

def anagram_gen(words):

    temp = []
    word = words.split(",")
    print(word)
    for i, letter in enumerate(word):
        for j in (word[:i]+word[i+1:]):
            print(word[:i])
            print(word[i+1:])
            temp.append(j+letter)
    print(temp)



if __name__ == '__main__':
    # this is for reverse str
    # words = str(sys.argv[1:]).replace("[","").replace("]","")
    # print(words)
    # uncomment this if wanna do the basic challenge for #1
    # words = sys.argv[1:]
    # print(words)
    # print(random_python(words))
    # print(reverse_word(words))

    # this is for mad libs
    words = sys.argv[1:][0]
    # print(words[1:])
    # mad_libs(words)
    anagram_gen(words)
