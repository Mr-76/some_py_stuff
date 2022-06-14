
def is_sorted(list1):
    
    first_item = 0
    for item in list1:
        if (first_item == 0):
            first_item = item
            continue

        else:
            if (first_item >= item):
                return False
            else:
                first_item = item
        return True  
        
                




def main():
    test_list = [1,2,3]
    test_list2 = ['a','b','c']
    test_list3 =  ['c','a','b']

    print(is_sorted(test_list))
    print(is_sorted(test_list2))
    print(is_sorted(test_list3))

if __name__ == "__main__":
    main()
