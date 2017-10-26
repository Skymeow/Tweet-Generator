import random, sys

with open('/usr/share/dict/words', 'r') as f:
    data = f.read()
    # splits at space
    dataList = data.split()

def get_words(letters):
    results = []
    for i in range(0, letters):
        rand_index = random.randint(0, len(dataList))
        results.append(dataList[rand_index])
    return(" ".join(results))

def auto_complete(letter):
    results = []
    for i in dataList:
        if i[0] == letter:
            results.append(i)
    return(" ".join(results))

if __name__ == '__main__':
    # get random num of letters from words file
    # num_letters = int(sys.argv[1:][0])
    # print(get_words(num_letters))

    # autocomplete
    letter = str(sys.argv[1:][0])
    print(auto_complete(letter))
