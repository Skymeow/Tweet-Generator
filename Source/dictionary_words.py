import random, sys

def get_words(letters):
    with open('/usr/share/dict/words', 'r') as f:
        data = f.read()
        # splits at space
        dataList = data.split()
        # print(dataList)
        results = []
        for i in range(0, letters):
            rand_index = random.randint(0, len(dataList))
            results.append(dataList[rand_index])
        return(" ".join(results))

if __name__ == '__main__':
    # get random num of letters from words file
    num_letters = int(sys.argv[1:][0])
    print(get_words(num_letters))
