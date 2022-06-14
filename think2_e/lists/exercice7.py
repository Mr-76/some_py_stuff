def has_duplicates(list1):
    for item in list1:
        soma = 0
        for item2 in list1:
            if (item2 == item):
                soma += 1
        if (soma >= 2):
            print("duplicate found")
            print("duplicate found is",item)
            return True
def main():
    test_list1 = [1,2,3]
    test_list2 = ['a','b','b']
    has_duplicates(test_list1)
    has_duplicates(test_list2)
if __name__ == '__main__':
    main()
