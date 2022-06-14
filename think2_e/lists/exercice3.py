

def middle(list1):
    list1.pop(-1)
    list1.pop(0)
    return list1

def main():
    list_test = [1,2,3,4]
    print(middle(list_test))

    

if __name__ == '__main__':
    main()
