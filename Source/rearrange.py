import random, sys



def random_python(words):
    result = []
    for i in range(0, len(words)):
        rand_index = random.randint(0, len(words)-1)
        result.append(words.pop(rand_index))
    return(' '.join(result))


if __name__ == '__main__':
    words = sys.argv[1:]
    print(random_python(words))

