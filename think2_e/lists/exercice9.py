import time

def list_words(file):
    list_of_words = []
    start = time.time()
    for line in file:
        word = line.strip()
        list_of_words.append(word)
    end  = time.time()
    print("timing to get it done",end)
    return list_of_words


def list_words2(file):
    list_of_words = []
    start = time.time()
    for line in file:
        word = line.strip()
        list_of_words = list_of_words + [word]
    end  = time.time()
    print("timing to get it done",end)
    return list_of_words

def main():
    with open('words.txt','r') as file:
        print(list_words2(file))
        print(list_words(file))

if __name__ == '__main__':
    main()
