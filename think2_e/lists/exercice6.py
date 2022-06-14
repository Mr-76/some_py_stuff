
def is_anagram(string1,string2):
    sum1 = 0
    sum2 = 0
    for item1,item2 in zip(string1,string2):
        sum1 += ord(item1)
        sum2 += ord(item2)
    if (sum1 == sum2):
        print("are anagrams")
        return True
    else:
        print("not anagrams")
        return False


def main():
    string1 = 'ana'
    string2 = 'naa'
    is_anagram(string1,string2)
    string3 = 'mamao'
    string4 = 'mamae'
    is_anagram(string3,string4)
if __name__ == '__main__':
    main()
