

def chop(list1):
    list1.pop(0)
    list1.pop(-1)




def main():
    test_list = [1,2,3,4]
    chop(test_list)
    print(test_list)

if __name__ == "__main__":
    main()
