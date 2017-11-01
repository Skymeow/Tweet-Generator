import random, sys, time
# with is closing file after read it
# or f = open.. and then have to f.close
# get a list of strings: f.readlines
# del array[index]: SAMPLING without replacement

# keep track of the start of run time
t_init = time.time()

# create a function to getWords
def create_words_list(filename):
    with open(filename, 'r') as f:
        data = f.read()
        # splits at space
        dataList = data.split()
    # rename to word_list nt
    return dataList

def get_words(letters, dataList):
    results = []
    for i in range(0, letters):
        rand_index = random.randint(0, len(dataList)).strip()
        results.append(dataList[rand_index])
    return(" ".join(results))

def auto_complete(letter, dataList):
    results = []
    for i in dataList:
        if i[0] == letter:
            results.append(i)
    return(" ".join(results))

if __name__ == '__main__':
    dataList = create_words_list("/usr/share/dict/words")
    # get random num of letters from words file
    # num_letters = int(sys.argv[1:][0])

    # to generate 3 sentences
    # for _ in range(3):
     # print(get_words(num_letters))

    # autocomplete
    letter = str(sys.argv[1:][0])
    print(auto_complete(letter, dataList))
    print("this is {} milisecond".format 1000*(time.time()-t_init))
